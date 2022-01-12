from rest_framework import serializers

from .models import User


class LoginSocialSerializer(serializers.Serializer):

    token_id = serializers.CharField(required=True)


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = (
            'id',
            'password',
            'username',
            'email',
            'first_name',
            'last_name',
            'gender',
            'phone',
            'city',
        )

