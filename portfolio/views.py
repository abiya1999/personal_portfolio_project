from django.shortcuts import render
from .models import Project
from .models import Course

def home(request):
    return render(request,'portfolio/home.html')

def about(request):
    return render(request,'portfolio/about.html')

def courses(request):
    projects = Project.objects.all()#grabs all objects from Project
    return render(request,'portfolio/courses.html',{'projects':projects})

def proj(request):
    pro = Course.objects.all()#grabs all objects from Project
    return render(request,'portfolio/proj.html',{'courses':pro})
