from tkinter import W
from django.contrib import admin

# Register your models here.
from . models import Profile, Skill,Worklog,Message,PersonalMeeting

admin.site.register(Profile)
admin.site.register(Skill)
admin.site.register(Worklog)
admin.site.register(Message)
admin.site.register(PersonalMeeting)