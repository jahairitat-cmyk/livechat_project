from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls', namespace='chat')),
    path('', RedirectView.as_view(url='/chat/', permanent=True)),
]