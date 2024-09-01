from django.urls import path
from . import views

urlpatterns = [
    path('', views.contactView, name='contact'),
    path('enviar-mensaje', views.formContactView, name='enviar-mensaje')
]