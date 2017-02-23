from __future__ import unicode_literals

from django.db import models
from ..loginRegister.models import User


class Course(models.Model):
	name = models.CharField(max_length=255)
	user = models.ManyToManyField(User)
	description = models.TextField(max_length = 1000)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)