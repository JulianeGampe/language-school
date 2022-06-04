from django.urls import path
from . import views


urlpatterns = [
    path('', views.checkout, name='checkout'),
    path(
        'checkoutsuccess/<ordernumber>',
        views.checkoutsuccess,
        name='checkoutsuccess'
    ),
]
