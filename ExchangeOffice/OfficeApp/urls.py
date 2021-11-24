from django.urls import path
from .views import response

urlpatterns = [
    path('main/', response),
]