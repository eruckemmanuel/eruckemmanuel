from django.shortcuts import render
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView


from home.models import ContactMessage
from home.serializers import ContactMessageSerializer
from home.utils import status_codes


class SaveMessage(APIView):

    permission_classes = [permissions.AllowAny]

    context = {}

    def post(self, request, *args, **kwargs):

        try:
            name = request.data['name']
            email = request.data['email']
            message = request.data['message']
        except Exception as e:
            print(e)
            self.context['status'] = 430
            self.context['status_text'] = status_codes[430]

            return Response(self.context)

        message = ContactMessage(name=name, email=email, message=message)
        message.save()
        self.context['status'] = 200
        self.context['status_text'] = status_codes[200]

        return Response(self.context)



class GetMessages(APIView):

    context = {}

    def get(self, request, *args, **kwargs):
        messages = ContactMessage.objects.all().order_by('-date')
        serializer = ContactMessageSerializer(messages, many=True)
        self.context['status'] = 200
        self.context['status_text'] = status_codes[200]
        self.context['data'] = serializer.data

        return Response(self.context)

