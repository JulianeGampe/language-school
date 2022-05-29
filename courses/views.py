from django.shortcuts import render
from .models import Course


def allcourses(request):
    courses = Course.objects.all()
    template = 'courses/courses.html'
    context = {
        'courses': courses
    }
    return render(request, template, context)
