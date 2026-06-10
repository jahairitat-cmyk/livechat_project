# chat/urls.py
from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('set_username/', views.set_username, name='set_username'), # Endpoint para guardar el username
    path('get_messages/', views.get_messages, name='get_messages'), # Endpoint para obtener mensajes
    path('send_message/', views.send_message, name='send_message'), # Endpoint para enviar mensajes
    path('room/', views.chat_room, name='chat_room'), # Vista para la sala de chat
    path('', views.username_input, name='username_input'), # Vista para la pantalla de entrada de username
]