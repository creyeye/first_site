from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('shishki/', views.shishka_list),
    path('shishka/<int:id>/', views.shishka_detail)
]
