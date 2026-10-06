from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('genero/<slug:slug>/', views.ver_peliculas, name='ver_peliculas'),
]