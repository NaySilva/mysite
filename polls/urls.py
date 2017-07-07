from django.conf.urls import url, include
from django.contrib import admin

from polls import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^question/(?P<question_id>\d+)$', views.exibir, name='exibir'),
    url(r'^question/(?P<question_id>\d+)/result$', views.result, name='result'),
    url(r'^question/(?P<question_id>\d+)/vote$', views.vote, name='vote'),
    url(r'^choice/(?P<choice_id>\d+)/votar$', views.votar, name='votar'),
    url(r'^question/(?P<question_id>\d+)/manage$', views.manage, name='manage'),
    url(r'^question/(?P<question_id>\d+)/mudar_status$', views.mudar_status, name='mudar_status'),
    url(r'^choice/(?P<choice_id>\d+)/remove$', views.remove, name='remove'),
]
