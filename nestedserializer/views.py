from django.shortcuts import render
from rest_framework import serializers,generics
from nestedserializer .serializers import CourseSerializer, InstructorSerializer
from rest_framework .response import Response
from nestedserializer.models import Instructor,Courses
from rest_framework.permissions import IsAuthenticated 
# IsAuthenticated:-provide session base authetication or basic authentication

# Create your views here.
class InstructorListView(generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer


class InstructorDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer

# ----------------------------------------------------------------------------------




class CourseListView(generics.ListCreateAPIView):
    
    queryset = Courses.objects.all()
    serializer_class = CourseSerializer

class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Courses.objects.all()
    serializer_class=CourseSerializer