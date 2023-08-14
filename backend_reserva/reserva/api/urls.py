from django.contrib import admin
from django.urls import path, include

app_name = 'reserva'
urlpatterns = [
    path('v1/',include("reserva.api.v1.urls")),
]
