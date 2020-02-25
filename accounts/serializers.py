from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    phone = serializers.SerializerMethodField()
    address = serializers.SerializerMethodField()
    city = serializers.SerializerMethodField()
    country = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()
    date_registered = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'id',
                  'phone', 'address', 'city', 'country', 'image', 'date_registered']

    def get_phone(self, user):
        return user.profile.phone

    def get_address(self, user):
        return user.profile.address

    def get_city(self, user):
        return user.profile.city

    def get_country(self, user):
        return user.profile.country

    def get_image(self, user):
        if user.profile.image:
            return user.profile.image.url
        return ''

    def get_date_registered(self, user):
        return user.profile.date_registered


