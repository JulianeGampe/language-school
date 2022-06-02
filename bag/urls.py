from django.urls import path
from . import views

urlpatterns = [
    path('', views.viewbag, name='viewbag'),
]
