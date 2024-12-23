from django.urls import path
from myresume import views

urlpatterns = [
    path('', views.home),  # http://127.0.0.1:8000/
    path('myresume/', views.index),  # http://127.0.0.1:8000/myresume/
]
