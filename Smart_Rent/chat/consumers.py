# chat/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # This room name can be static since it's a one-to-one chat with you
        self.room_group_name = "personal_chat_room"

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        name = text_data_json.get("name")
        message = text_data_json.get("message")

        # Broadcast message to the room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "name": name,
                "message": message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        name = event["name"]
        message = event["message"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            "name": name,
            "message": message
        }))