from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, FileResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import ItemsInfo, ReportInfo
from datetime import date
import json
import os



@login_required
def control_panel(requset: HttpRequest):
    if requset.method == 'POST':
        itemName = requset.POST.get('itemName')
        itemQuantity = requset.POST.get('itemQuantity')
        ItemsInfo.objects.create(name_item=itemName,quantity_item=itemQuantity)
        return redirect('http://127.0.0.1:8000/control_panel/')
    else:
        items = ItemsInfo.objects.all()
        info_items = {}
        for item in items:
            info_items[item.id] = [item.name_item, item.quantity_item]
        print(info_items)
        return render(requset, 'control_panel.html', {'info_items': info_items})
    
def delete_item(request: HttpRequest):
    if request.method == 'POST':
        data_json = json.loads(request.body)
        print(data_json)
        print(data_json['id_item'])
        ItemsInfo.objects.filter(id=data_json['id_item']).delete()
        return redirect('http://127.0.0.1:8000/control_panel/')
    
def handle_uploaded_file(f):
    with open(f"reports_file//{f.name}", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)

@login_required
def reports(request: HttpRequest):
    if request.method == 'POST':
        file_upload = request.FILES['file_report']
        date_upload_file = date.today()
        with open('usernick-username.json', 'r', encoding='utf-8') as file_json: # в json файле должны быть имена сотрудников
            json_file_username = json.load(file_json)
            try:
                name_user_json = json_file_username[request.user.username]
            except KeyError:
                return HttpResponse("<h1>Сотрудник не добавлен в файл. Доступ запрещен</h1>")
        ReportInfo.objects.create(
            name_report_file=file_upload.name, 
            name_user=name_user_json,
            date_upload_report=date_upload_file
            )
        return redirect('http://127.0.0.1:8000/control_panel/reports')
    else:
        data_reports = {}
        report_info = ReportInfo.objects.all()
        for objects in report_info:
            data_reports[objects.name_report_file] = [objects.date_upload_report, objects.name_user]
        return render(request, 'reports.html', {'data_reports': data_reports})

@login_required
def download_report(request: HttpRequest, file_name):
    return FileResponse(open(f'reports_file//{file_name}', 'rb'), as_attachment=True)

@login_required
def delete_report(request:HttpRequest):
    if request.method == 'POST':
        data_json = json.loads(request.body)
        print(data_json)
        ReportInfo.objects.filter(name_report_file=data_json['name_file']).delete()
        os.remove(f'reports_file/{data_json['name_file']}')
        return redirect('http://127.0.0.1:8000/control_panel/reports')