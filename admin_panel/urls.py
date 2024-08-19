from django.urls import path
from .views import *


urlpatterns = [
    path('', index),
    path('control_user/', control_user),
    path('control_user/add_user/', add_user),
    path('control_user/delete_user/', delete_user)
    
]