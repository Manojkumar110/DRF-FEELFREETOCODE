from django.contrib import admin
from django.urls import path
from api.views import employeeDetailView, employeeListView,user

urlpatterns = [
    path('/employee',employeeListView),
    path('/employee/<int:pk>',employeeDetailView),
    path('user/',user),
    
]
