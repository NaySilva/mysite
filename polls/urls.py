from django.conf.urls import url, include
from django.contrib import admin

from polls import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^question/(?P<question_id>\d+)$', views.exibir, name='exibir'),
]
