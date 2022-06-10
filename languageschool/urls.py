from django.contrib import admin
from django.urls import path, include
from .views import handler404, handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('courses/', include('courses.urls')),
    path('bag/', include('bag.urls')),
    path('checkout/', include('checkout.urls')),
    path('profile/', include('profiles.urls')),
    path('teachers/', include('teachers.urls')),
    path('courseinfo/', include('courseinfo.urls')),
    path('contact/', include('contact.urls')),
]
handler404 = 'languageschool.views.handler404'
handler500 = 'languageschool.views.handler500'
