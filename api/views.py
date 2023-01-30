from django.shortcuts import render
from django .http import JsonResponse ,HttpResponse
from django .contrib.auth.models import User
from api.models import Employee
from api.serializers import EmployeeSerializer, UserSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q
# Create your views here.

# Employee Get And Update View :-
# @csrf_exempt # Ignore csrf token .
@api_view(['GET','POST'])
def employeeListView(request):
    if request.method == 'GET':
        emp = Employee.objects.all()
        serializer = EmployeeSerializer(emp,many=True)
        return JsonResponse(serializer.data,safe=False)

    elif request.method == 'POST':
        jsonData = JSONParser().parse(request)
        nationality = jsonData.get('Natioanlity')
        if nationality == 'INDIAN':
            serializer = EmployeeSerializer(data=jsonData)
        elif nationality == 'indian':
            serializer = EmployeeSerializer(data=jsonData)
        else:
            return JsonResponse('Natioanlity Not Match',safe=False)

        if serializer.is_valid():
            serializer.save()
        else:
            return JsonResponse(serializer.errors,safe=False)
        return JsonResponse(serializer.data,safe=False)

# Employee Detail View :-
# @csrf_exempt
@api_view(['GET','PUT','DELETE'])
def employeeDetailView(request , pk=None):
    try:
        employee = Employee.objects.get(pk=pk)
    except Exception as e:
        return Response('Employee Does Not Exist')

    if request.method =='GET':
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        employee.delete()
        return Response(status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        jsonData =  JSONParser().parse(request) 
        # serializer = EmployeeSerializer(employee,data=request.data)
        serializer = EmployeeSerializer(employee,data=jsonData)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        else: 
            return JsonResponse(serializer.errors)
       





# User Views :-
@api_view(['GET'])
def user(request):
    user = User.objects.all()
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data)