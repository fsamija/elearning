from django.conf.urls import patterns, url
from course import views
import course.views

urlpatterns = [
    url(r'^$', course.views.ListCourseView.as_view(),
        name='courses-list',),
url(r'^new/$', course.views.CreateCourseView.as_view(),
    name='courses-new',),
 url(r'^edit/(?P<pk>\d+)/$', course.views.UpdateCourseView.as_view(),
        name='courses-edit',),
 url(r'^delete/(?P<pk>\d+)/$', course.views.DeleteCourseView.as_view(),
        name='courses-delete',),
 # url(r'^view/(?P<pk>\d+)/$', course.views.DetailCourseView.as_view(),
 #        name='courses-view',),
 #  url(r'^view1/(?P<pk>\d+)/$', course.views.show_files,
 #        name='courses-view1',),
	]

