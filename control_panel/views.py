from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, FileResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import ItemsInfo, ReportInfo
from os import listdir
from datetime import date



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
    
@login_required   
def handle_uploaded_file(f):
    with open(f"reports_file/{f.name}", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)
@login_required
def reports(request: HttpRequest):
    if request.method == 'POST':
        file = request.FILES['file_report']
        handle_uploaded_file(file)
        date_upload_file = date.today()
        ReportInfo.objects.create(
            name_report_file=file, 
            name_user=request.user.username,
            date_upload_report=date_upload_file
            )
        
        names_file = listdir('reports_file/')
        print(names_file)
        return render(request, 'reports.html', {'names_file': names_file})
        
    names_file = listdir('reports_file/')
    print(names_file)
    return render(request, 'reports.html', {'names_file': names_file})

@login_required
def download_report(request: HttpRequest, file_name):
    return FileResponse(open(f'reports_file/{file_name}', 'rb'), as_attachment=True)