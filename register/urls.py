from django.urls import path
from .views import *

urlpatterns = [
    path('', register),
    path('logout', log_out),
    path('login', log_in)
]
