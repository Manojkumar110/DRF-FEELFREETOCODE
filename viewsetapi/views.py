from django.shortcuts import render
from rest_framework .viewsets import ViewSet,ModelViewSet

from classbaseview .models import Cloth
from classbaseview  .serializers import ClothSerializer
from rest_framework .response import Response

# Create your views here.


# 1.viewset
# 2.modelview set


# 1.viewset start Here

class ViewSetApi(ViewSet):
    def list(self , request):
        cloth= Cloth.objects.all()
        serializer = ClothSerializer(cloth , many=True)
        return Response(serializer.data)
    
    def retrieve(self , request , pk):
        try:
            cloth = Cloth.objects.get(pk=pk)
            serializer = ClothSerializer(cloth)
            return Response(serializer.data)
        except Exception as e:
            return Response('Object Does Not Exist.')

    def create(self,request):
        # jasonData = JSONParser().parse(request)
        serializer = ClothSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response('Data Not Valid.')
            
# Viewset End Here




# model view set statr here

class modelViewSetApi(ModelViewSet):
    queryset = Cloth.objects.all()
    serializer_class = ClothSerializer



# model view set end here