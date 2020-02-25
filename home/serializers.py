from home.models import ContactMessage
from rest_framework import serializers


class ContactMessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactMessage
        fields = '__all__'