from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date

# Create your models here.

class Announcement(models.Model):
	date = models.DateTimeField(auto_now_add=True)
	announcement = models.TextField()

class Event(models.Model):
	date = models.DateTimeField()
	event_name = models.CharField(max_length=100)
	event_description = models.TextField()
	event_image = models.ImageField()

	def __str__(self):
		return self.event_name

class Feedback(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
	feedback = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	comment = models.TextField(blank=True, null=True)
