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
    path('fc/', views.fc, name='fc'),
    path('bwc/', views.bwc, name='bwc'),
    path('senate/', views.senate, name='senate'),
    path('deans/', views.deans, name='deans'),
    path('administration/', views.administration, name='administration'),
    path('planning/', views.planning, name='planning'),
    path('architecture/', views.architecture, name='architecture'),
    path('fic/', views.fic, name='fic'),
    path('health/', views.health, name='health'),
]
