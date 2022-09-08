from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('noticeboard/', views.noticeboard, name='noticeboard'),
    path('registration/', views.registration, name='registration'),
    path('director/', views.director, name='director'),
    path('chairperson/', views.chairperson, name='chairperson'),
    path('computer-center/', views.cc, name='cc'),
    path('actsandstatutes/', views.actsnstatute, name='actsnstatute'),
    path('bog/', views.bog, name='bog'),
]
