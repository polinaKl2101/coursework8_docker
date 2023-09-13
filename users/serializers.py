from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from users.models import User


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, value):
        value['password'] = make_password(value.get('password'))
        return super().create(value)

    class Meta:
        model = User
        fields = '__all__'
