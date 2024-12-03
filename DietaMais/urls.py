from django.urls import path
from . import views

urlpatterns = [
    path('listar/', views.listarAlimentos, name='listarAlimentos'),
    path('cadastrar/', views.cadastrarAlimentos, name='cadastrarAlimentos'),
]
