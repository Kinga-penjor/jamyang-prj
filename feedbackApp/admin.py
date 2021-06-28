from django.contrib import admin
from . models import *
from django.contrib.auth.models import Group

# Register your models here.

admin.site.unregister(Group)

admin.site.site_header = "Administration"

admin.site.register(Announcement)
admin.site.register(Event)
admin.site.register(Feedback)