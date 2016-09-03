from __future__ import unicode_literals

from django.db import models

# Create your models here.
BOOLS = ((True,'Yes'),(False,'No'))
class Todo(models.Model):
	name = models.CharField(max_length = 100, unique = True)
	created = models.DateTimeField(auto_now_add = True, auto_now = False)
	description = models.TextField(blank = True)
	completed = models.BooleanField(default = False, choices=BOOLS)

	def __str__(self):
		return self.name

	def __unicode__(self):
		return self.name