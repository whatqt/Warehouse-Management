from django.shortcuts import render, redirect
from django.http import HttpRequest, JsonResponse
from .decoratos import check_staff
import json
from django.contrib.auth.models import User




@check_staff
def index(request: HttpRequest):
    return render(request, 'admin_panel.html')

@check_staff
def add_and_ref_user(requset: HttpRequest):
    if requset.method == 'POST':
        print('POST')
        usernick = requset.POST.get('newusernick')
        userlastname = requset.POST.get('newuserlastname')
        with open('usernick-username.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            
        data.update({usernick: userlastname})
        with open('usernick-username.json', 'w', encoding='utf-8') as file:
            json.dump(data, file)

        return redirect('http://127.0.0.1:8000/admin_panel/add_user/')
    
    else:
        with open('usernick-username.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            print(data)
        return render(requset, 'add_user.html', {'data': data})
    
@check_staff
def delete_user(request: HttpRequest):
    pass