from django.http import HttpResponse
from django.shortcuts import render



def home(request):  # HttpRequest
    return HttpResponse('<h1>Главная страница</h1>')


def myresume(request, my_id):  # HttpRequest
    return HttpResponse(f'<h3>Страница приложения myresume</h3><p>id: {my_id}</p>')


def myresume_by_slug(request, my_slug):  # HttpRequest
    return HttpResponse(f'<h3>Страница приложения myresume</h3><p>slug: {my_slug}</p>')


def archive (request, year):
    return HttpResponse(f'<h3>Архив по годам</h3><p>{year}</p>')
