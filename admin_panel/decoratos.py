from django.http import HttpResponse
import json


def check_staff(input_func):
    def check_staff_true(*args):
        print(*args)
        request = args[0]
        if request.user.is_staff:
            return input_func(*args)
        else:
            return HttpResponse('Ошибка', status=404)
    return check_staff_true

# with open('C:\\Users\\trutn\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.12\\python23\\django\\warehouse_management\\usernick-username.json', 'r', encoding='utf-8') as file:
#     data = json.load(file)
#     print(data)