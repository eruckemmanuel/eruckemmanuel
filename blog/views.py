"""
API views for the Blog App
"""

from django.shortcuts import render


from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions, status



class PostView(APIView):

    context = {}

    def get(self, request, *args, **kwargs):
        pass


    def post(self, request, *args, **kwargs):
        pass
