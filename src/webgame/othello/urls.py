from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='othello-index'),
    path('vscpu/<int:level>/', views.vscpuHome, name='othello-vscpuHome'),
    path('vscpu/<int:level>/create', views.vscpuCreate, name='othello-vscpuCreate'),
    path('vscpu/<int:level>/<int:gameId>/', views.vscpuShow, name='othello-vscpuShow'),
    path('vscpu/<int:level>/<int:gameId>/sendchat', views.vscpuSendChat, name='othello-vscpuSendChat'),
    path('vscpu/<int:level>/<int:gameId>/getchat', views.vscpuGetChat, name='othello-vscpuGetChat'),
    path('vscpu/<int:level>/<int:gameId>/getboard', views.vscpuGetBoard, name='othello-vscpuGetBoard'),
]