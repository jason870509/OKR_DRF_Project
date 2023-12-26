from rest_framework import serializers
from django.contrib.auth.models import User


class UserPublicSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(read_only=True)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
        ]


    def validate_password(self, value):
        password = self.context['request'].data['password']
        password2 = self.context['request'].data['password2']

        if password != password2:
            raise serializers.ValidationError("Passwords are not the same. Please Check.")

        return super().validate(value)