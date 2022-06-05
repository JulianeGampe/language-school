from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path(
        'orderhistory/<ordernumber>', views.orderhistory, name='orderhistory'
    ),
]
