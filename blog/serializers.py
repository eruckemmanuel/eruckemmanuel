"""
Serializers for the blog app
"""

from rest_framework import serializers
from blog.models import Post


""" Serializer class for the Post Model """
class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'