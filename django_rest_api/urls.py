
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api',include('api.urls')),
    path('',include('api.urls')),
    path('',include('courseapi.urls')),
    path('',include('classbaseview.urls')),
    path('',include('viewsetapi.urls')),
    path('',include('nestedserializer.urls'))
]
