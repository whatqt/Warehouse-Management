from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, FileResponse, JsonResponse
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
        return redirect('http://127.0.0.1:8000/control_panel/')
        # return render(requset, 'control_panel.html', {'info_items': info_items}) 
    else:
        items = ItemsInfo.objects.all()
        info_items = {}
        for item in items:
            info_items[item.id] = [item.name_item, item.quantity_item]
        print(info_items)
        return render(requset, 'control_panel.html', {'info_items': info_items})
    
def delete_item(request: HttpRequest):
    print('первый этап1')
    if request.method == 'POST':
        print('второй этап2')
        # print(request.body)
        data = json.loads(request.body)
        print(data)
        print(data['id_item'])
        ItemsInfo.objects.filter(id=data['id_item']).delete()
        # items = ItemsInfo.objects.all()
        # info_items = {}
        # for item in items:
        #     info_items[item.id] = [item.name_item, item.quantity_item]
        # #если удаляется один объект, то вызывается ошибка VM372:1 Uncaught (in promise) SyntaxError: Unexpected token 'e', "test" is not valid JSON
        # return render(request, 'control_panel.html', {'info_items': info_items})
        # return JsonResponse({'tru': 'tru'})
        return redirect('http://127.0.0.1:8000/control_panel/')
    
def handle_uploaded_file(f):
    with open(f"reports_file//{f.name}", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)

@login_required
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

@login_required
def download_report(request: HttpRequest, file_name):
    return FileResponse(open(f'reports_file/{file_name}', 'rb'), as_attachment=True)

