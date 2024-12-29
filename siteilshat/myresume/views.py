from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse



def home(request):  # HttpRequest
    return HttpResponse('<h1>Главная страница</h1>')


def myresume(request, my_id):  # HttpRequest
    return HttpResponse(f'<h3>Страница приложения myresume</h3><p>id: {my_id}</p>')


def myresume_by_slug(request, my_slug):  # HttpRequest
    return HttpResponse(f'<h3>Страница приложения myresume</h3><p>slug: {my_slug}</p>')


def archive(request, year):
    if year > 2024:
        uri = reverse('myresume_slug', args=('music', ))
        return redirect('/')

    return HttpResponse(f'<h3>Архив по годам</h3><p>{year}</p>')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1?')
