from django.urls import path
from . import views

urlpatterns = [
    path('', views.TableClientsView, name='table-clients')
]