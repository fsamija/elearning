"""e URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include, patterns
from django.conf.urls.static import static
from django.contrib import admin
import course.views
from django.contrib.auth import views as auth_views
from django.views.static import serve

urlpatterns = [
# url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^$', course.views.IndexView.as_view(), name='index'),
	url(r'^admin/', admin.site.urls),
	url(r'^course/', include('course.urls')),
	url(r'^accounts/login/$', auth_views.login),
	url(r'^logout/$', auth_views.logout),
	url(r'^register/$', course.views.register , name="register"),
	#url(r'^groups-manager/', include('groups_manager.urls', namespace='groups_manager')),
    url(r'^media/(?P<path>.*)$',serve,
        {'document_root': settings.MEDIA_ROOT}),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),

    
]
# if settings.DEBUG:
# 	urlpatterns += patterns('django.views.static',
#         (r'^media/(?P<path>.*)$',
#         serve,
#         {'document_root': settings.MEDIA_ROOT}),)