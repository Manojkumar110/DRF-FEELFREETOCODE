from django.contrib import admin
from django.urls import path,include
from viewsetapi .views import ViewSetApi,modelViewSetApi
from rest_framework .routers import DefaultRouter


router = DefaultRouter()
router.register('viewsetapi',ViewSetApi,basename='ViewSetApi')
router.register('modelviewsetapi',modelViewSetApi,basename='modelviewsetapi')
urlpatterns = [
    path('',include(router.urls))

]
