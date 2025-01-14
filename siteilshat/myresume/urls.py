from django.urls import path, re_path, register_converter
from myresume import views, converters


register_converter(converters.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('', views.home, name='home'),  # http://127.0.0.1:8000/
    path('about/', views.about, name='about'),
    path('addpage/', views.addpage, name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('post/<slug:post_slug>/', views.show_post, name='post'),
    path('category/<int:cat_id>/', views.show_category, name='category'),
    # path('myresume/<int:my_id>/', views.myresume, name='myresume_id'),  # http://127.0.0.1:8000/myresume/123/
    # path('myresume/<slug:my_slug>/', views.myresume_by_slug, name= 'myresume_slug'),  # http://127.0.0.1:8000/myresume/qerty123/
    # path('archive/<year4:year>/', views.archive, name='archive'),
]
