from django.urls import path
from . import views


urlpatterns = [
    path('', views.allcourses, name='allcourses'),
]
