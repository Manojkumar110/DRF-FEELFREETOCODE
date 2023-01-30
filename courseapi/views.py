from django.shortcuts import render
from django .http import HttpResponse , JsonResponse
from api.serializers import CourseSerializer
from courseapi .models import Course
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

# Create your views here.



# Functions Base view:-

@api_view(['GET','POST'])
def CourseListView(request):
    if request.method == 'GET':
        couser = Course.objects.all()
        serializer = CourseSerializer(couser , many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        jsonData = JSONParser().parse(request)
        serializer = CourseSerializer(data=jsonData)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        else:
            return JsonResponse('Please Enter Valid Information..')

@api_view(['GET','PUT','DELETE'])
def CourseDetailView(request ,pk):
    try:
        course = Course.objects.get(pk=pk)
    except Exception as e:
        return JsonResponse('Course Not Found..',safe=False)
    if request.method == 'GET':
        seriliazer = CourseSerializer(course)
        return JsonResponse(seriliazer.data , safe=False)
    elif request.method == 'DELETE':
        course.delete()
        return JsonResponse('Course Not Available..')
    elif request.method == 'PUT':
        JsonData = JSONParser().parse(request)
        seriliazer = CourseSerializer(course,data=JsonData)
        if seriliazer.is_valid():
            seriliazer.save()
            return JsonResponse(seriliazer.data)

# End Funsctions Base View here:-

