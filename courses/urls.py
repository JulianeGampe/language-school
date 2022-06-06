from django.urls import path
from . import views


urlpatterns = [
    path('', views.allcourses, name='allcourses'),
    path('<int:course_id>/', views.coursedetail, name='coursedetail'),
    path('add/', views.addcourse, name='addcourse'),
    path('edit/<int:course_id>', views.editcourse, name='editcourse'),
    path('delete/<int:course_id>', views.deletecourse, name='deletecourse'),
]
