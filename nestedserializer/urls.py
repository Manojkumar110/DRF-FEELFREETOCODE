from django.contrib import admin
from django.urls import path,include
from nestedserializer .views import CourseDetailView, InstructorListView,CourseListView,InstructorDetailView
urlpatterns = [
    path('instructor',InstructorListView.as_view()),
    path('nscourselist',CourseListView.as_view()),
    path('nscourselist/<int:pk>',CourseDetailView.as_view(), name='courses-detail'),
    path('instructor/<int:pk>',InstructorDetailView.as_view(), name='instructor-detail')
]
