from django import urls
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('insta', views.insta),
]
