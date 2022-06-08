from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Course
from .forms import CourseForm
from profiles.models import UserProfile


def allcourses(request):
    """
    View to display all courses
    """
    courses = Course.objects.all()
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            courses = courses.order_by(sortkey)

    current_sorting = f'{sort}_{direction}'

    template = 'courses/courses.html'
    context = {
        'courses': courses,
        'current_sorting': current_sorting
    }
    return render(request, template, context)


def coursedetail(request, course_id):
    """
    View to display details of one course
    """
    course = get_object_or_404(Course, pk=course_id)
    if request.user.is_authenticated:
        profile = get_object_or_404(UserProfile, user=request.user)
        orders = profile.orders.all()

        template = 'courses/course_detail.html'
        context = {
            'course': course,
            'orders': orders,
        }
    else:
        template = 'courses/course_detail.html'
        context = {
            'course': course,
        }
    return render(request, template, context)


@login_required
def addcourse(request):
    """
    View to add a course from the frontend
    """
    if not request.user.is_superuser:
        messages.error(request, 'Access denied.')
        return redirect('home')

    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully added the course')
            return redirect('allcourses')
        else:
            messages.error(
                request, 'Failed to add course. Please check the form'
            )
    else:
        form = CourseForm()

    template = 'courses/add_course.html'
    context = {
        'form': form
    }
    return render(request, template, context)


@login_required
def editcourse(request, course_id):
    """
    View to edit a course
    """
    if not request.user.is_superuser:
        messages.error(request, 'Access denied.')
        return redirect('home')

    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        editform = CourseForm(request.POST, instance=course)
        if editform.is_valid():
            editform.save()
            messages.success(
                request, 'You have successfully updated the course'
            )
            return redirect('allcourses')
        else:
            messages.error(
                request, 'Failed to update course. Please check the form'
            )

    else:
        editform = CourseForm(instance=course)

    template = 'courses/edit_course.html'
    context = {
        'editform': editform,
        'course': course
    }

    return render(request, template, context)


@login_required
def deletecourse(request, course_id):
    """
    View to delete a course.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Access denied.')
        return redirect('home')

    course = get_object_or_404(Course, pk=course_id)
    template = "courses/delete_course.html"
    context = {
        'course': course
    }

    if request.method == 'POST':
        course.delete()
        messages.success(request, 'Course successfully deleted!')
        return redirect('allcourses')
    return render(request, template, context)
