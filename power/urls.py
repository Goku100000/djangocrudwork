from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', include("work/urls.py")),
]
