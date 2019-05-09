from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='othello-index'),
    path('vscpu/<int:level>', views.vscpu, name='othello-vscpu'),
]