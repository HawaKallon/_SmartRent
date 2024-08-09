from django.urls import path
from .views import ChatRoomView

app_name = 'chat'

urlpatterns = [
    path('room/', ChatRoomView.as_view(), name='chat_room'),
]