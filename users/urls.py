from django.urls import path, include
from . import views as users_views
from django.contrib import admin

urlpatterns = [
    path('', users_views.index, name='index'),
]
