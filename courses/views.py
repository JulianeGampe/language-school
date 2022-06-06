from django.shortcuts import render, get_object_or_404, redirect
from .models import Course
from .forms import CourseForm


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


def addcourse(request):
    """
    View to add a course from the frontend
    """
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('allcourses')
    else:
        form = CourseForm()

    template = 'courses/add_course.html'
    context = {
        'form': form
    }
    return render(request, template, context)


def editcourse(request, course_id):
    """
    View to edit a course
    """
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        editform = CourseForm(request.POST, instance=course)
        if editform.is_valid():
            editform.save()
            return redirect('allcourses')

    else:
        editform = CourseForm(instance=course)

    template = 'courses/edit_course.html'
    context = {
        'editform': editform,
        'course': course
    }

    return render(request, template, context)


def deletecourse(request, course_id):
    """
    View to delete a course.
    """
    course = get_object_or_404(Course, pk=course_id)
    template = "courses/delete_course.html"
    context = {
        'course': course
    }

    if request.method == 'POST':
        course.delete()
        return redirect('allcourses')
    return render(request, template, context)
