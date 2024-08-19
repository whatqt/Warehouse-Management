from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .decoratos import check_staff


@check_staff
def index(request: HttpRequest):
    return render(request, 'admin_panel.html')