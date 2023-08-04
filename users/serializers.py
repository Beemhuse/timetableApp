# accounts/serializers.py
from rest_framework import serializers
from .models import CustomUser

class SignUpSerializer(serializers.ModelSerializer):
    user_type = serializers.ChoiceField(choices=CustomUser.USER_TYPE_CHOICES)

    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'user_type')
        extra_kwargs = {'password': {'write_only': True}}
