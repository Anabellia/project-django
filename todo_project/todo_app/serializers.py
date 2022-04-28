from dataclasses import fields
from rest_framework import serializers
from todo_app.models import User


# Model Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name')
