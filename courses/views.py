from django.shortcuts import render, get_object_or_404
from .models import Course


def allcourses(request):
    """
    View to display all courses
    """
    courses = Course.objects.all()
    template = 'courses/courses.html'
    context = {
        'courses': courses
    }
    return render(request, template, context)


def coursedetail(request, course_id):
    """
    View to display details of one course
    """
    course = get_object_or_404(Course, pk=course_id)
    template = 'courses/course_detail.html'
    context = {
        'course': course
    }
    return render(request, template, context)
