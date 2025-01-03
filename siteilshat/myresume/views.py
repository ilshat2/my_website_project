from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify


menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'add_page'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'},
]

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


def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи с id = {post_id}')


def addpage(request):
    return HttpResponse('Добавление статьи')


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Авторизация')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1?')
