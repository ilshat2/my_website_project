from django.urls import path, re_path, register_converter
from myresume import views, converters


register_converter(converters.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('', views.home, name='home'),  # http://127.0.0.1:8000/
    path('myresume/<int:my_id>/', views.myresume, name='myresume_id'),  # http://127.0.0.1:8000/myresume/123/
    path('myresume/<slug:my_slug>/', views.myresume_by_slug, name= 'myresume_slug'),  # http://127.0.0.1:8000/myresume/qerty123/
    path('archive/<year4:year>/', views.archive, name='archive')
]
