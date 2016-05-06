from __future__ import unicode_literals
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission, Group
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from embed_video.fields import EmbedVideoField

def upload_location(obj, filename):
	return "%s/%s" %(obj.course, filename)

class Course(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
	title = models.CharField(max_length=255,)	
	# list_display = ('display_courses')
	# fieldsets = [(None, 
	# 	{'fields': ['chapter_title']}),
	# ('Date information', {'fields': ['pub_date']}),
	# ('Content', {'fields': ['content']}),
	# ]
	# list_display = ('chapter_title', 'pub_date', 'content')
	def __str__(self):
		return ' '.join([
			self.title
			])
	class Meta:
		permissions = (
			('can_view', 'Can View'),
			('can_modify', 'Can Modify'),
			('can_create', 'Can Create'),
			('can_delete', 'Can Delete'),
			('can_list', 'Can See List'),
			)

	# def display_file(self):
	# 	self.upload.open() # reset the pointer of file, needs if you need to read file more than once, in a request.
	# 	return self.upload.read().replace('\n', '<br>')
class CourseChapter(models.Model):
	subtitle = models.CharField(max_length=255,)
	content = models.CharField(max_length=255,)
	course = models.ForeignKey(Course, blank=True)#, on_delete=models.CASCADE, related_name="course_chapters"#)
	upload = models.FileField(upload_to=upload_location, blank=True)
	video = EmbedVideoField(blank=True)
	image = models.ImageField(upload_to=upload_location, blank=True)
	html = RichTextField(blank=True,)
	# HTML = 1
	# IMAGE = 2
	# VIDEO = 3
	# QUIZ = 4
	# CONTENT_CHOICES = (
	# 	(HTML, 'HTML'),
	# 	(IMAGE, 'Image'),
	# 	(VIDEO, 'Video'),
	# 	(QUIZ, 'Quiz'),
	# 	)
	# choice = models.IntegerField(choices=CONTENT_CHOICES, default=HTML)
	# def display_courses(self):
	# 	return ', '.join([ course.name for course in self.courses.all() ])
	def __str__(self):       
		return self.subtitle


class UserProfile(models.Model):
	user = models.OneToOneField(User)

	picture = models.ImageField(upload_to='profile_images', blank=True)

	class Meta:
		permissions = ( ('add_course', 'Add course'), )

	def __unicode__(self):
		return self.user.username

# students = Group(name='Students')
# students.save()
# professor = Group.objects.get(name='Professors')
#professor.save()
#really_special_users = Group(name='Super Special Users')
#really_special_users.save()

# somemodel_ct = ContentType.objects.get(app_label='course', model='course')

# can_view = Permission(name='Can View', codename='can_view_something',
#                        content_type=somemodel_ct)
#can_view.save()

# can_modify = Permission(name='Can Modify', codename='can_modify_something',
#                        content_type=somemodel_ct)

# can_create = Permission(name='Can Create', codename='can_create_something',
#                        content_type=somemodel_ct)

# can_delete = Permission(name='Can Delete', codename='can_delete_something',
#                        content_type=somemodel_ct)

# can_shit = Permission(name='Can Shit', codename='can_shit_something',
#                        content_type=somemodel_ct)
# can_shit.save()
# can_delete.save()


#professor.permissions = [can_shit, can_delete]
# really_special_users.permissions = [can_view, can_modify]


#jack=User.objects.get(email='jack@test.com')
#jack.groups.add(proffesor)

# jill=User.objects.get(email='jill@test.com')
# jill.groups.add(really_special_users)
# class Entity(models.Model):
#     class Meta:
#         # Remove default permissions, remove this line to keep them
#         default_permissions = dict()

#         # Custom permissions 
#         permissions = (
#             ("add_democourse", "Add new demo course"),
#             ("edit_democourse", "Edit demo course"),
#             ("delete_democourse", "Delete demo course"),
#             ("list_democourse", "See list of demo courses"),
#             ("view_democourse", "View demo course profile"),
#         )

#     user = models.OneToOneField(User)
#     parent = models.ManyToManyField(User, related_name='parents', blank=True)