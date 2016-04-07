from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission, Group
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.conf import settings

def upload_location(obj, filename):
	return "%s/%s" %(obj.user, filename)

class Course(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	name = models.CharField(
		max_length=255,
		)
	upload = models.FileField(upload_to=upload_location, blank=True)

	def __str__(self):
		return ' '.join([
			self.name
			])
	class Meta:
		permissions = (
			('can_view', 'Can View'),
			('can_modify', 'Can Modify'),
			('can_create', 'Can Create'),
			('can_delete', 'Can Delete'),
			)
	# def display_file(self):
	# 	self.upload.open() # reset the pointer of file, needs if you need to read file more than once, in a request.
	# 	return self.upload.read().replace('\n', '<br>')
	

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
