from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/chat/personal_chat_room/', consumers.ChatConsumer.as_asgi()),
]