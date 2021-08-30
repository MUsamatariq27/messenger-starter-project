
from django.db import models

from . import utils



class MessageRecepient(utils.CustomModel):
    receipientId =  models.IntegerField(),
    senderId =  models.IntegerField(),
    conversationId = models.IntegerField(),
    messageId = models.IntegerField(),
    createdAt = models.DateTimeField(auto_now_add=True, db_index=True)
    updatedAt = models.DateTimeField(auto_now=True)