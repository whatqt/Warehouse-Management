from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


@login_required
def index(request: HttpRequest):
    return render(request, 'index.html')

def register(request: HttpRequest):
    if request.method == "POST":
        username = request.POST.get('username').replace(' ', '')
        password = request.POST.get('password').replace(' ', '')
        check_replay_name = User.objects.filter(username=username)
        if check_replay_name:
            return HttpResponse('<h1>Такой ник занят</h1>')
        User.objects.create_user(username=username, password=password)
        auth = authenticate(request, username=username, password=password)
        print(auth)
        login(request, auth)
        return HttpResponse('<h1>Вы зарегистрировались</h1>')
    return render(request, 'register.html')

@login_required    
def log_out(requset: HttpRequest):
    logout(requset)
    return redirect('http://127.0.0.1:8000/register/login')

def log_in(request: HttpRequest):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        auth = authenticate(request, username=username, password=password)
        print(auth)
        if auth:
            check_is_staff = User.objects.get(username=username).is_staff
            if check_is_staff:
                login(request, auth)
                return redirect('http://127.0.0.1:8000/admin_panel/')
            login(request, auth)
            return redirect('http://127.0.0.1:8000/')
        else:
            return HttpResponse('<h1>Неправильный логин или пароль</h1>')
    return render(request, 'login.html')
 
