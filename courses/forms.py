from django import forms
from .models import Course


class CourseForm(forms.ModelForm):
    """
    CourseForm to add a course from the frontend
    """
    class Meta:
        model = Course
        fields = '__all__'
