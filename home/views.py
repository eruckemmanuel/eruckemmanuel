from django.shortcuts import render
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView


class SaveMessage(APIView):

    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        pass
