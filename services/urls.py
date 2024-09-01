from django.urls import path
from . import views

urlpatterns = [
    path('', views.servicesView, name='services'),
    path('service-detail/<int:pk>/', views.serviceDetailView, name='service-detail'),
]