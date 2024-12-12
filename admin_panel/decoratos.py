from django.http import HttpResponse


def check_staff(input_func):
    def check_staff_true(*args):
        print(*args)
        request = args[0]
        if request.user.is_staff:
            return input_func(*args)
        else:
            return HttpResponse('Ошибка', status=404)
    return check_staff_true

