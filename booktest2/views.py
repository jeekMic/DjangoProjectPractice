from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
# Create your views here.
def login_ajax(request):
    return render(request, 'booktest2/login_ajax.html')


def login_ajax_check(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username)
    print(password)
    if username=='smart' and password=='123':
        return  JsonResponse({'res':1})
    else:
        return JsonResponse({'res':0})
