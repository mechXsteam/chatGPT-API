# chat/views.py
import os

from dotenv import load_dotenv
from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Chat, Message
from .serializers import ChatSerializer, MessageSerializer
from .utils import get_response

load_dotenv()

openai_secret_key = os.getenv("OPENAI_API_KEY")


class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Get response using context
        chat = Chat.objects.get(id=serializer.validated_data['chat'].id)
        response = get_response(serializer.validated_data['prompt'], chat.context)

        # Here, you can save the generated response to the message or take other actions
        # For this example, I'm assuming the 'response' field in the serializer can be populated
        serializer.validated_data['response'] = response

        # Save the message
        self.perform_create(serializer)
        print("serializer valid data:", serializer.validated_data)
        # Update chat context
        chat.context += serializer.validated_data['prompt'] + serializer.validated_data['response'].content
        chat.save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
