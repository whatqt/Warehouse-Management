from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, FileResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import ItemsInfo, ReportInfo
from os import listdir
from datetime import date
import json



@login_required
def control_panel(requset: HttpRequest):
    if requset.method == 'POST':
        itemName = requset.POST.get('itemName')
        itemQuantity = requset.POST.get('itemQuantity')
        ItemsInfo.objects.create(name_item=itemName,quantity_item=itemQuantity)
        items = ItemsInfo.objects.all()
        info_items = {}
        for item in items:
            info_items[item.id] = [item.name_item, item.quantity_item]
        print(info_items) 
        return render(requset, 'control_panel.html', {'info_items': info_items}) 
    else:
        items = ItemsInfo.objects.all()
        info_items = {}
        for item in items:
            info_items[item.id] = [item.name_item, item.quantity_item]
        print(info_items)
        return render(requset, 'control_panel.html', {'info_items': info_items})
    
def handle_uploaded_file(f):
    with open(f"reports_file//{f.name}", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def reports(request: HttpRequest):
    if request.method == 'POST':
        file = request.FILES['file_report']
        print(file.name)
        handle_uploaded_file(file)
        date_upload_file = date.today()
        with open('usernick-username.json', 'r', encoding='utf-8') as js:
            json_file_username = json.load(js)
            name = json_file_username[request.user.username]
        # в панели админа добавить возможность добавлять ник пользователя и его реально имя для того, чтобы в БД заносилось Ф.И.О пользователя 
        print(name)
        ReportInfo.objects.create(
            name_report_file=file, 
            name_user=name,
            date_upload_report=date_upload_file
            )
        data_reports = {}
        report_info = ReportInfo.objects.all()
        for objects in report_info:
            data_reports[objects.name_report_file] = [objects.date_upload_report, objects.name_user]
        return render(request, 'reports.html', {'data_reports': data_reports})
        
    data_reports = {}
    report_info = ReportInfo.objects.all()
    for objects in report_info:
        data_reports[objects.name_report_file] = [objects.date_upload_report, objects.name_user]
    return render(request, 'reports.html', {'data_reports': data_reports})

def download_report(request: HttpRequest, file_name):
    return FileResponse(open(f'reports_file/{file_name}', 'rb'), as_attachment=True)