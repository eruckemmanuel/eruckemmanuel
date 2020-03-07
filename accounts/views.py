from random import randint

from django.utils import timezone
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
from accounts.tasks import send_sms




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
            self.context['status'] = 406
            self.context['data'] = 'INVALID VERIFICATION'
            return Response(self.context)


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



class VerifyPhoneNumber(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        context = {}
        phone = request.GET.get('phone')
        code = ''.join(["{}".format(randint(0, 9)) for num in range(0, 6)])

        message = _('Your Account Verifcation Code is V-')+code +'.\n'+_('Enter this code in the text field.')

        PhoneVerificationCodes.objects.filter(phone=phone).update(expired=True)

        sent = send_sms('VehMail', phone, message)
        if sent:
            PhoneVerificationCodes(phone=phone, code=code,
                                   date_sent=timezone.now()).save()

            context['status'] = 200
            context['status_text'] = status_codes[200]
        else:
            context['status'] = 500
            context['status_text'] = status_codes[500]

        return Response(context)




class ValidateVerificationCode(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        context = {}
        phone = request.GET.get('phone')
        code = request.GET.get('code')

        match = PhoneVerificationCodes.objects.filter(Q(phone=phone) & Q(code=code)
                                                      & Q(verified=False) & Q(expired=False))
        if match:
            context['status'] = 202
            context['status_text'] = status_codes[202]
            match.update(verified=True)
        else:
            context['status'] = 406
            context['status_text'] = status_codes[406]

        return Response(context)




def get_user(username):
    user = User.objects.filter(username=username)
    if user:
        return user[0]