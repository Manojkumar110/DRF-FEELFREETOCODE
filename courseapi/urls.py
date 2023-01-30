from django.contrib import admin
from django.urls import path,include
from courseapi .views import CourseDetailView, CourseListView
urlpatterns = [
    path('courselistview',CourseListView),
    path('couserdetail/<int:pk>/',CourseDetailView)
]