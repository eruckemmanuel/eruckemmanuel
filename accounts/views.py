from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions, status
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django.db.models import Q
from django.db import transaction


from accounts.models import Profile, PhoneVerificationCodes
from accounts.serializers import UserSerializer


from home.utils import status_codes




class GetAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})

        serializer.is_valid(raise_exception=False)

        try:
            user = serializer.validated_data['user']
        except KeyError as e:
            user = None

        if user:
            print('user found')
            serialized_user = UserSerializer(user)

            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'status':200,
                'status_text':status_codes[200],
                'data':{
                    'token': token.key,
                    'user': serialized_user.data
                }

            })
        else:
            print('no user found')
            return Response({
                'status':403,
                'status_text':status_codes[403]
            })




class CreateAccount(APIView):
    permission_classes = [permissions.AllowAny]
    context = {}


    @transaction.atomic
    def post(self, request, *args, **kwargs):

        try:
            first_name = request.data['first_name']
            last_name = request.data['last_name']
            username = request.data['username']
            phone = request.data['phone']
            address = request.data['address']
            city = request.data['city']
            country = request.data['country']
            password = request.data['password']
            code = request.data['code']
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        match = PhoneVerificationCodes.objects.filter(Q(phone=phone) & Q(code=code)
                                                      & Q(verified=False) & Q(expired=False))
        if not match:
            self.context['data'] = 'INVALID VERIFICATION'
            return Response(self.context, status=status.HTTP_406_NOT_ACCEPTABLE)


        if get_user(username):
            self.context['data'] =  _('USERNAME ALREADY EXIST')
            return Response(self.context, status=status.HTTP_406_NOT_ACCEPTABLE)

        user = User.objects.create_user(username, username, password)
        user.first_name = first_name
        user.last_name = last_name

        Profile(user=user, phone=phone, city=city, country=country,
                address=address).save()

        serialized_user = UserSerializer(user)

        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'data': {
                'token': token.key,
                'user': serialized_user.data
            }

        })


def get_user(username):
    user = User.objects.filter(username=username)
    if user:
        return user[0]