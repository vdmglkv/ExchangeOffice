from django.urls import path
from . import views
urlpatterns = [
    path('', views.main),
    path('change/', views.change),
    path('contact/', views.contact),
    path('currencyrate/', views.currency_rate),
    path('client/', views.client),
]
