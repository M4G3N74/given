from django.shortcuts import render
from django.urls import path
from .views import  HomeView
# Create your views here.

urlpatterns = [
    path('', HomeView.as_view()),
]