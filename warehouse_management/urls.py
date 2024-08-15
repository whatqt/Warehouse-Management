from django.contrib import admin
from django.urls import path, include 
from register.views import index



urlpatterns = [
    path('', index),
    path('register/', include('register.urls')),
    path('control_panel/', include('control_panel.urls'))
]
