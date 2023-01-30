from django.shortcuts import render
from django .http import HttpResponse
from rest_framework .response import Response
from rest_framework .views import APIView
from classbaseview .models import Cloth
from classbaseview .serializers import ClothSerializer
from rest_framework .parsers import JSONParser
from rest_framework import mixins,generics


# Class Base View:- 
'''
class ClothListView(APIView):
    def get(self,request):
        print('Get Method Call..')
        cloth = Cloth.objects.all()
        serializer = ClothSerializer(cloth,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        jsonData = JSONParser().parse(request)
        serializer = ClothSerializer(data = jsonData)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response('Please Post Valid Data')


class ClothDetailView(APIView):
    def get(self ,request, pk):
        try:
            cloth = Cloth.objects.get(pk=pk)
            serializer = ClothSerializer(cloth)
            return Response(serializer.data)
        except Exception as e:
            return Response('Item Dose Not Exist.')
    def put(self , request , pk):
        cloth = Cloth.objects.get(pk=pk)
        jasonData = JSONParser().parse(request)
        serializer = ClothSerializer(cloth,data=jasonData)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response('please Provide Valid Data.')

    def delete(self , request , pk):
        cloth = Cloth.objects.get(pk=pk)
        cloth.delete()
        return Response('Product Delete.')
'''
# End Class Base View Here :-
# ---------------------------------------------------------------------


# Mixing Start Here:-

# mixing Class:-
'''
1.ListModelMixin = list()
2.CreateModelMixin = create()
3.RetrieveModelMixin = retrieve()
4.UpdateModelMixin = update()
5.DestroyModelMixin = destroy()
'''
'''
class ClothListView(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Cloth.objects.all()
    serializer_class = ClothSerializer
    def get(self , request):
        return self.list(request)

    def post(self,request):
        return self.create(request)

class ClothDetailView(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Cloth.objects.all()
    serializer_class = ClothSerializer

    def get(self,request,pk):
        return self.retrieve(request,pk)


    def put(self,request,pk):
        return self.update(request,pk)
    

    def delete(self,request,pk):
        return self.destroy(request,pk)
'''


# End here Mixins :-



# Generic Action: -


class ClothListView(generics.ListCreateAPIView):
    queryset = Cloth.objects.all()
    serializer_class = ClothSerializer


class ClothDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cloth.objects.all()
    serializer_class = ClothSerializer 

# View Set Action :-




