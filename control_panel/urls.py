from django.urls import path
from .views import *



urlpatterns = [
    path('', control_panel),
    path('reports', reports),
    path('reports/delete_report', delete_report),
    path('download_report/<file_name>', download_report),
    path('delete_item',delete_item)
]
