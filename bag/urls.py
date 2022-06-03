from django.urls import path
from . import views

urlpatterns = [
    path('', views.viewbag, name='viewbag'),
    path('add/<course_id>/', views.addbag, name='addbag'),
    path('remove/<course_id>/', views.removebag, name='removebag'),
]
