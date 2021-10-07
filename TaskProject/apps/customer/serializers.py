# from .models import User
from django.contrib.auth import get_user_model
from rest_framework import serializers

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username','password']
        extra_fields ={'password':{'write_only':True},}

    # def create(self,validated_data):

    #     return get_user_model().objects.create_user(**validated_data)

class LoginSerializer(serializers.Serializer):
    username= serializers.CharField(max_length=10)
    password = serializers.CharField(max_length=50,read_only=True)
    token =serializers.CharField(max_length=300, read_only=True)

# class UserCreateSerilizer()