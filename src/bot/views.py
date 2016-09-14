from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    if request.method == 'GET':
        return HttpResponse('HOLA JIMBO!')
    elif request.method == 'POST':
        return HttpResponse('')
