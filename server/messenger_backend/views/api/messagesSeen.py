from django.http import HttpResponse, JsonResponse
from messenger_backend.models import Conversation, Message
from rest_framework.views import APIView
from django.contrib.auth.middleware import get_user
import datetime, pytz




class Messageseen(APIView):
    
    def put(self, request, conversationId: str):
    
        try:
            user = get_user(request)

            if user.is_anonymous:
                return HttpResponse(status=401)
            
            if (conversationId is None):
                return HttpResponse(status=400)

            conversation = Conversation.objects.filter(id=conversationId).first()

            lastIndex = len(conversation.messages.all()) - 1
            latestMessage = conversation.messages.all()[lastIndex]

            if (latestMessage.senderId == user.id):
                return HttpResponse(status=204)
            
            for message in conversation.messages.all():
                
                if (message.seen is None):
                    message.seen = datetime.datetime.now(tz=pytz.timezone("US/Eastern"))
                    message.save()
            
            return JsonResponse({"success" : True})
            
        except Exception as e:
            return HttpResponse(status=500)
    