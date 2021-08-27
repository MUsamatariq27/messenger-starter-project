from django.http import HttpResponse, JsonResponse
from messenger_backend.models import Conversation, Message
from rest_framework.views import APIView
from django.contrib.auth.middleware import get_user
import datetime, pytz

class  MessagesSeen(APIView):
    
    def put(self, request, conversationId: str, otherUserId: str):
    
        try:
            user = get_user(request)

            if user.is_anonymous:
                return HttpResponse(status=401)
            
            if (conversationId is None):
                return HttpResponse(status=400)

            convoCheck = Conversation.find_conversation(user.id, otherUserId)

            if ( (convoCheck is None) or (convoCheck.id != int(conversationId))):
                return HttpResponse(status=404)

            conversationMessages = Conversation.objects.filter(id=conversationId).first().messages.all()

            lastIndex = len(conversationMessages) - 1
            latestMessage = conversationMessages[lastIndex]
            if (latestMessage.senderId == user.id):
                return HttpResponse(status=204)
            
            dateTime=datetime.datetime.now(tz=pytz.timezone("US/Eastern"))
            conversationMessages.filter(seen=None).update(seen=dateTime)

        
            
            return JsonResponse({"success" : True})
            
        except Exception as e:
            return HttpResponse(status=500)