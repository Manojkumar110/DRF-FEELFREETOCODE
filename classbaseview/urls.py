
from django.contrib import admin
from django.urls import path,include
from classbaseview .views import ClothListView,ClothDetailView  
urlpatterns = [
    path('cloth/',ClothListView.as_view()),
    path('cloth/<int:pk>',ClothDetailView.as_view())
]
