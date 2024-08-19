from django.urls import path
from .views import *


urlpatterns = [
    path('', index),
    path('add_user/', add_and_ref_user)
]