from dataclasses import fields
from rest_framework import serializers
from todo_app.models import MyUser
from django.contrib.auth.models import User


# Model Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id', 'first_name', 'last_name')


class UserAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
