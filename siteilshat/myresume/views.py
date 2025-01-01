from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify

menu = {'О сайте', 'Добавить статью', 'Обратная связь', 'Войти'}


data_db = [
    {'id': 1, 'title': 'Telegram Bot', 'content': 'Бот который раз в 10 минут опрашивает API', 'is_published': True},
    {'id': 2, 'title': 'API Yamdb', 'content': 'RestAPI для сервиса Yamdb - базы данных книг, музыки, фильмов.', 'is_published': False},
    {'id': 3, 'title': 'yamdb_final', 'content': 'web-приложение и базу данных, поднятых в двух docker-контейнерах', 'is_published': True},
]


def home(request):  # HttpRequest
    data ={
        'title': 'Главная страница',
        'menu': menu,
        'posts': data_db,
    }
    return render(request, 'myresume/index.html', context=data)


def about(request):
    return render(request, 'myresume/about.html', {'title': 'О сайте'})


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
