from rest_framework import serializers
from django.contrib.auth.models import User
from django_app import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ['url', 'username', 'email', 'is_staff']
        fields = '__all__'

class TextModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TextModel
        fields = '__all__'