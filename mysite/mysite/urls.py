from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('apex.urls')),
    path('admin/', admin.site.urls),
]
