from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home-index'),
    path('send_data', views.sendData, name='home-sendData'),
]