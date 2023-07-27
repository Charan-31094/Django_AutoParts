from django.shortcuts import render

# Create your views here.
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('ad/', admin.site.urls),

    path("", include("app1.urls")),
]
from django.shortcuts import render

# Create your views here.
