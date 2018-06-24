from rest_framework import serializers
from gituserlib.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('date_joined', 'email', 'username', 'is_active')