"""
Imports for PyPi modules
"""
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

"""
Imports for project Models
"""
from home.models import ContactMessage


"""
Imports for Project Serializers
"""
from home.serializers import ContactMessageSerializer




"""View for processing Contact Messages of Site"""
class ContactMessage(APIView):

    permission_classes = [permissions.AllowAny]

    context = {}

    def post(self, request, *args, **kwargs):

        try:
            name = request.data['name']
            email = request.data['email']
            message = request.data['message']
        except KeyError as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        message = ContactMessage(name=name, email=email, message=message)
        message.save()

        self.context['message'] = ContactMessageSerializer(message).data

        return Response(self.context, status=status.HTTP_200_OK)


    def get(self, request, *args, **kwargs):

        if not request.user.is_authenticated:
            return Response(status=status.HTTP_403_FORBIDDEN)

        messages = ContactMessage.objects.all().order_by('-date')
        serializer = ContactMessageSerializer(messages, many=True)

        self.context['messages'] = serializer.data

        return Response(self.context, status=status.HTTP_200_OK)


