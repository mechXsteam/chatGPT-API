# chat/models.py

from django.contrib.auth.models import User
from django.db import models


class Chat(models.Model):
    user = models.EmailField(unique=True)
    chat_title = models.CharField(max_length=500, default='new chat')
    context = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.chat_title}"


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    prompt = models.TextField()
    response = models.TextField(blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.prompt} {self.response}'
