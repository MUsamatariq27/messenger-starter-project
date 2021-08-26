from django.db import models
#from django.db.models.fields import BooleanField

from . import utils
from .conversation import Conversation


class Message(utils.CustomModel):
    text = models.TextField(null=False)
    senderId = models.IntegerField(null=False)
    conversation = models.ForeignKey(
        Conversation,
        on_delete=models.CASCADE,
        db_column="conversationId",
        related_name="messages",
        related_query_name="message"
    )
    seen = models.DateTimeField(null=True)
    createdAt = models.DateTimeField(auto_now_add=True, db_index=True)
    updatedAt = models.DateTimeField(auto_now=True)