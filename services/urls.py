from django.urls import path
from . import views

urlpatterns = [
    path('', views.servicesView, name='services'),
    path('service-detail/', views.serviceDetailView, name='service-detail'),
]