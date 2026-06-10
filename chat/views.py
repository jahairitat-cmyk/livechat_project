from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Message

def username_input(request):
    return render(request, 'chat/username_input.html')

def set_username(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        if username:
            request.session['username'] = username
            return HttpResponseRedirect(reverse('chat:chat_room'))
    return HttpResponseRedirect(reverse('chat:username_input'))

def chat_room(request):
    return render(request, 'chat/chat_room.html')

def get_messages(request):
    messages = Message.objects.all().order_by('timestamp')
    data = [
        {'username': msg.username, 'content': msg.content, 'timestamp': msg.timestamp.strftime('%Y-%m-%d %H:%M:%S')}
        for msg in messages
    ]
    return JsonResponse(data, safe=False)

def send_message(request):
    if request.method == 'POST':
        username = request.session.get('username', 'Anonymous')
        content = request.POST.get('content')
        if content:
            Message.objects.create(username=username, content=content)
            return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)