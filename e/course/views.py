from django.shortcuts import render, redirect 
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.views import generic
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView, TemplateView
from course.models import Course
from django.core.urlresolvers import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from django.contrib.auth.forms import UserCreationForm
from e.forms import MyRegistrationForm, UserProfileForm, UserForm
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from models import UserProfile
from braces.views import GroupRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth import models
from django.conf import settings
from django.core.files import File
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class IndexView(generic.ListView):
	template_name = 'course/index.html'
	def get_queryset(self):
		return 

def is_professor(user):
    return user.groups.filter(name='Professors').exists()
# def group_required(arg_name):
#     def decorator(view):
#         def wrapper(request, *args, **kwargs):
#             group_id = kwargs.get(arg_name)
#             user = request.user
#             if group_id in user.groups.values_list('id', flat=True):
#                 return view(request, *args, **kwargs)
#             else:
#                 return HttpResponseForbidden # 403 Forbidden is better than 404
#         return wrapper
#     return decorator

# @login_required
# @user_passes_test(is_professor)
# PAGINACIJA, NE RADI view
# def ListCourseView(request):
# 	queryset_list = Course.objects.all()
# 	paginator = Paginator(queryset_list, 25) # Show 25 
# 	query = request.GET.get("query")
# 	if query:
# 		queryset_list = queryset_list.filter(name__icontains=query)
# 	page = request.GET.get('page')
# 	try:
# 		queryset = paginator.page(page)
# 	except PageNotAnInteger:
# 		queryset = paginator.page(1)
# 	except EmptyPage:		
# 		queryset = paginator.page(paginator.num_pages)

# 	return render_to_response('course/course_list.html', {"object_list": queryset})

class DetailCourseView(DetailView):
	model = Course
	#template_name = 'course/course_view.html'

def show_files(request, pk):
	objects = Course.objects.get(id=pk)
	return render_to_response('course/course_view.html', {'objects': objects},
	                              context_instance=RequestContext(request))


class ListCourseView(ListView):
	# group_required = u"Professor"
	model = Course
	template_name = 'course/course_list.html'
	fields = '__all__'
	def get_queryset(self):
		# if not self.request.user.is_superuser:
		# 	return HttpResponseForbidden()
		queryset_list = Course.objects.all()		
		query = self.request.GET.get("query")
		if query:
			queryset_list = queryset_list.filter(name__icontains=query)
		
		paginator = Paginator(queryset_list, 10) # Show 25 
		page = self.request.GET.get('page')
		try:
			queryset = paginator.page(page)
		except PageNotAnInteger:
			queryset = paginator.page(1)
		except EmptyPage:		
			queryset = paginator.page(paginator.num_pages)

		return queryset

	def get_context_data(self, **kwargs):
		context = super(ListCourseView, self).get_context_data(**kwargs)
		return context

	def get_success_url(self):
		return reverse('courses-list')

	#return render(request, template_name)

# @user_passes_test(is_professor)	
# def CreateCourseView(request):
	
# 	# def get_queryset(self, request):
# 	# 	if not request.user.is_superuser:
# 	# 		return False

# 	model = Course
# 	template_name = 'course/edit_course.html'
# 	fields = '__all__'

# 	def get_success_url(self):
# 		return reverse('courses-list')

# 	def get_context_data(self, **kwargs):

# 		context = super(CreateCourseView, self).get_context_data(**kwargs)
# 		context['action'] = reverse('courses-new')
# 		return context

# 	return render(request, template_name)

class CreateCourseView(CreateView, GroupRequiredMixin):
	# def get_queryset(self, request):
	# 	if not request.user.is_superuser:
	# 		return False
	

	model = Course
	template_name = 'course/edit_course.html'
	fields = '__all__'

	#required_permissions = (u'course.can_create')

	@method_decorator(permission_required('course.can_create',raise_exception=True))
	def dispatch(self, request):
		return super(CreateCourseView, self).dispatch(request)
	def get_success_url(self):
		return reverse('courses-list')

	def get_context_data(self, **kwargs):

		context = super(CreateCourseView, self).get_context_data(**kwargs)
		context['action'] = reverse('courses-new')

		return context

class UpdateCourseView(UpdateView):

	model = Course
	template_name = 'course/edit_course.html'
	fields = '__all__'

	@method_decorator(permission_required('course.can_modify',raise_exception=True))
	def dispatch(self, request, pk):
		return super(UpdateCourseView, self).dispatch(request)

	def get_success_url(self):
		return reverse('courses-list')

	def get_context_data(self, **kwargs):

		context = super(UpdateCourseView, self).get_context_data(**kwargs)
		context['action'] = reverse('courses-edit',
                                    kwargs={'pk': self.get_object().id})

		return context

class DeleteCourseView(DeleteView):

	model = Course
	template_name = 'course/delete_course.html'

	@method_decorator(permission_required('course.can_delete',raise_exception=True))
	def dispatch(self, request, pk):
		return super(DeleteCourseView, self).dispatch(request)

	def get_success_url(self):
		return reverse('courses-list')



def register(request):


    registered = False
    
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

       
        if user_form.is_valid() and profile_form.is_valid():
           
            user = user_form.save()
            user.set_password(user.password)
            user.save()
           
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
        
            profile.save()         
            registered = True
       
        else:
            print user_form.errors, profile_form.errors
  
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    
    return render(request,
            'registration/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )