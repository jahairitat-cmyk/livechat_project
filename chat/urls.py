from django.urls import path
from . import views

urlpatterns = [
    path('set_username/', views.set_username, name='set_username'),
    path('get_messages/', views.get_messages, name='get_messages'),
    path('send_message/', views.send_message, name='send_message'),
    path('room/', views.chat_room, name='chat_room'),
    path('', views.username_input, name='username_input'),
]