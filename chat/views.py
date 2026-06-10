# chat/views.py
import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Message

def username_input(request):
    # Renderiza la plantilla para la entrada del nombre de usuario
    return render(request, 'chat/username_input.html')

def set_username(request):
    # Guarda el nombre de usuario en la sesión y redirige a la sala de chat
    if request.method == 'POST':
        username = request.POST.get('username')
        if username:
            request.session['username'] = username
            return HttpResponseRedirect(reverse('chat:chat_room'))
    return HttpResponseRedirect(reverse('chat:username_input')) # Redirigir si no es POST o falta username

def chat_room(request):
    # Renderiza la plantilla de la sala de chat
    return render(request, 'chat/chat_room.html')

def get_messages(request):
    # Recupera todos los mensajes de la base de datos
    messages = Message.objects.all().order_by('timestamp')
    # Formatea los mensajes para enviarlos como JSON
    data = [
        {'username': msg.username, 'content': msg.content, 'timestamp': msg.timestamp.strftime('%Y-%m-%d %H:%M:%S')}
        for msg in messages
    ]
    return JsonResponse(data, safe=False)

def send_message(request):
    # Crea un nuevo mensaje y lo guarda en la base de datos
    if request.method == 'POST':
        username = request.session.get('username', 'Anonymous') # Obtiene username de la sesión
        try:
            data = json.loads(request.body)
            content = data.get('content')
        except (json.JSONDecodeError, ValueError):
            content = request.POST.get('content')
        if content:
            Message.objects.create(username=username, content=content)
            return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)