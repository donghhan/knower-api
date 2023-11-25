from rest_framework import serializers
from .models import KnowerUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = KnowerUser
        fields = "__all__"
