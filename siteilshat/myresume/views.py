from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string

menu = {'О сайте', 'Добавить статью', 'Обратная связь', 'Войти'}


class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

def home(request):  # HttpRequest
    # t = render_to_string('myresume/index.html')
    # return HttpResponse(t)
    data ={
        'title': 'Главная страница',
        'menu': menu,
        'float': 84.37,
        'lst': [1, 2, 'abc', True],
        'set': {1, 2, 4, 8, 18},
        'dict': {'key_1': 'value_1', 'key_2': 'value_2'},
        'obj': MyClass(10, 20),
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
