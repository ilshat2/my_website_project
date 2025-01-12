from operator import index

from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify
from myresume.models import Myresume


menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'add_page'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'},
]

data_db = [
    {'id': 1, 'title': 'Telegram Bot', 'content': '''<h1>Telegram Bot</h1> который:
        раз в 10 минут опрашивает API сервиса Практикум.Домашка и проверяет статус отправленной на ревью домашней работы;
        при обновлении статуса анализирует ответ API и отправляет вам соответствующее уведомление в Telegram;
        логирует свою работу и сообщает вам о важных проблемах сообщением в Telegram. ''', 'is_published': True},
    {'id': 2, 'title': 'API Yamdb', 'content': 'RestAPI для сервиса Yamdb - базы данных книг, музыки, фильмов.', 'is_published': False},
    {'id': 3, 'title': 'yamdb_final', 'content': 'web-приложение и базу данных, поднятых в двух docker-контейнерах', 'is_published': True},
]

cats_db = [
    {'id': 1, 'name': 'Проекты'},
    {'id': 2, 'name': 'Резюме'},
    {'id': 3, 'name': 'Контакты'},
]


def home(request):  # HttpRequest
    data ={
        'title': 'Главная страница',
        'menu': menu,
        'posts': data_db,
        'cat_selected': 0,
    }
    return render(request, 'myresume/index.html', context=data)


def about(request):
    return render(request, 'myresume/about.html', {'title': 'О сайте', 'menu': menu})


def show_post(request, post_id):
    post = get_object_or_404(Myresume, pk=post_id)

    data = {
        'title': post.title,
        'menu': menu,
        'post': post,
        'cat_selected': 1,
    }
    return render(request, 'myresume/post.html', data)


def addpage(request):
    return HttpResponse('Добавление статьи')


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Авторизация')


def show_category(request, cat_id):
    data = {
        'title': 'Отображение по рубрикам',
        'menu': menu,
        'posts': data_db,
        'cat_selected': cat_id,
    }
    return render(request, 'myresume/index.html', context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1?')
