from django.contrib import admin

#import the models
from .models import Project
from .models import Course

admin.site.register(Project)
admin.site.register(Course)
