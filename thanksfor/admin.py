from django.contrib import admin
from thanksfor.models import Submission
from functions import *
import os
def rotate_clock_wise(modeladmin, request, queryset):
    submissions = list(queryset)
    for submission in submissions:
        rotateImageClockWise(submission)
rotate_clock_wise.short_description = "Rotate Clock-wise"

def rotate_counter_clock_wise(modeladmin, request, queryset):
    submissions = list(queryset)
    for submission in submissions:
        rotateImageCounterClockWise(submission)
rotate_counter_clock_wise.short_description = "Rotate Counter Clock-wise"

class SubmissionAdmin(admin.ModelAdmin):

    fields = ('created_at', 'image', 'image_thumb', 'name', 'email', 'ip_address','location', 'show_in_site' , 'user_agent')
    list_display = ('created_at', 'image', 'image_thumb','name', 'email','location','show_in_site',)
    readonly_fields=('image_thumb')
    
    actions = [rotate_clock_wise, rotate_counter_clock_wise]

admin.site.register(Submission, SubmissionAdmin)
