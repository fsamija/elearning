from braces.views import GroupRequiredMixin
from course.models import Course, UserProfile, CourseChapter
from django import forms
from django.conf import settings
from django.contrib.auth import models
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files import File
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, redirect, render_to_response,  get_object_or_404
from django.template import RequestContext
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView, TemplateView
from e.forms import MyRegistrationForm, UserProfileForm, UserForm, CourseForm, CourseChapterForm, CourseChapterFormSet



class IndexView(generic.ListView):
	template_name = 'course/index.html'
	def get_queryset(self):
		return 

# def is_professor(user):
#     return user.groups.filter(name='Professors').exists()
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

# class DetailCourseView(DetailView):
# 	model = Course
	#template_name = 'course/course_view.html'

# def show_files(request, pk):
# 	objects = Course.objects.get(id=pk)
# 	return render_to_response('course/course_view.html', {'objects': objects},
# 	                              context_instance=RequestContext(request))


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
		
		paginator = Paginator(queryset_list, 10) # Show 10
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
class CreateChapterView(CreateView, GroupRequiredMixin):
	model = CourseChapter
	template_name = 'course/add_chapter.html'
	fields = '__all__'
	def dispatch(self, request, *args, **kwargs):
		self.pk = kwargs.get('pk')
		return super(CreateChapterView, self).dispatch(request, *args, **kwargs)
	def get_success_url(self):
		return reverse('courses-list')

	def get_context_data(self, **kwargs):

		context = super(CreateChapterView, self).get_context_data(**kwargs)
		context['chapter'] = CourseChapterForm

		return context

	def form_valid(self, form):
		self.object = form.save()
		chapters = CourseChapter.objects.all()
		return  render_to_response('course/add_chapter.html', 
                          {'form': form, 'chapters': chapters}, context_instance = RequestContext(self.request))

class CreateCourseView(CreateView, GroupRequiredMixin):
	# def get_queryset(self, request):
	# 	if not request.user.is_superuser:
	# 		return False
	
	# form_class = CourseForm #umisto fields ako nije form_classes
	model = Course #netriba ako se koristi form_class ??
	template_name = 'course/edit_course.html'
	fields = '__all__'
	# chapter_form = CourseChapterForm()
	#required_permissions = (u'course.can_create')

	@method_decorator(permission_required('course.can_create',raise_exception=True))
	def dispatch(self, request, *args, **kwargs):
		self.pk = kwargs.get('pk')
		return super(CreateCourseView, self).dispatch(request, *args, **kwargs)
	def get_success_url(self):
		# course = get_object_or_404(Course, pk=course.id)
		return reverse('courses-chapters', kwargs={'pk': self.pk})

	def get_context_data(self, **kwargs):

		context = super(CreateCourseView, self).get_context_data(**kwargs)
		context['action'] = reverse('courses-new')
		context['chapter'] = CourseChapter.objects.all()
		return context

	def form_valid(self, form):
		# context = self.get_context_data()
		# formset = context['action']
		# if formset.is_valid():
		self.object = form.save()
		# 	formset.instance = self.object
		# 	formset.save()
		return HttpResponseRedirect(reverse('courses-chapters', kwargs={'pk': self.object.pk}))  # redirect(self.object.get_absolute_url()) assuming your model has ``get_absolute_url`` defined.
		# else:
		# 	return self.render_to_response(self.get_context_data(form=form))
	# def get_context_data(self, **kwargs):

	# 	context = super(CreateCourseView, self).get_context_data(**kwargs)
	# 	context['action'] = reverse('courses-new')

	# 	return context

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

		# context = super(UpdateCourseView, self).get_context_data(**kwargs)
		# if self.request.POST:
		# 	context['formset'] = CourseChapterFormSet(self.request.POST)
		# 	context['action'] = reverse('courses-edit',
  #                                   kwargs={'pk': self.get_object().id})
		# else:
		# 	context['formset'] = CourseChapterFormSet()
		# return context
		# def get_context_data(self, **kwargs):

		context = super(UpdateCourseView, self).get_context_data(**kwargs)
		# context['chapter'] = CourseChapterForm(self.request.POST)
		context['action'] = reverse('courses-edit',
                                    kwargs={'pk': self.get_object().id})
		context['chapter'] = CourseChapter.objects.get(course_id=self.get_object().id)

		return context
	def form_valid(self, form):
		self.object = form.save()
		return HttpResponseRedirect(self.get_success_url())

class UpdateChapterView(UpdateView):

	model = CourseChapter
	template_name = 'course/add_chapter.html'
	fields = '__all__'

	@method_decorator(permission_required('course.can_modify',raise_exception=True))
	def dispatch(self, request, pk):
		return super(UpdateChapterView, self).dispatch(request)

	def get_success_url(self):
		return reverse('courses-list')

	def get_context_data(self, **kwargs):

		context = super(UpdateChapterView, self).get_context_data(**kwargs)
		# context['chapter'] = CourseChapterForm(self.request.POST)
		context['action'] = reverse('chapters-edit',
                                    kwargs={'pk': self.get_object().id})

		return context
	def form_valid(self, form):
		self.object = form.save()
		return HttpResponseRedirect(self.get_success_url())

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