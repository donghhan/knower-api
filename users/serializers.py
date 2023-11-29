from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import KnowerUser


class UserSerializer(serializers.ModelSerializer):
    date_joined = serializers.ReadOnlyField()

    class Meta:
        model = KnowerUser
        fields = "__all__"


class CreateAccountSerializer(serializers.ModelSerializer):
    date_joined = serializers.ReadOnlyField()
    password = serializers.CharField(
        min_length=8,
        max_length=16,
        write_only=True,
        label="비밀번호",
        help_text="최소 8글자, 최대 16글자로 구성",
    )
    confirm_password = serializers.CharField(
        min_length=8, max_length=16, write_only=True, label="비밀번호 확인"
    )

    class Meta:
        model = KnowerUser
        fields = [
            "pk",
            "email",
            "first_name",
            "last_name",
            "mobile_number",
            "date_joined",
            "password",
            "confirm_password",
        ]

    def create(self, validated_data):
        user = KnowerUser.objects.create(
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            mobile_number=validated_data["mobile_number"],
            password=make_password(validated_data["password"]),
        )
        return user

    def validate(self, attrs):
        if attrs.get("password") != attrs.get("confirm_password"):
            raise serializers.ValidationError(
                "비밀번호가 일치하지 않습니다(CreateAccountSerializer Error)"
            )
        return attrs


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        min_length=8,
        max_length=16,
        required=True,
        write_only=True,
        style={"input_type": "password"},
    )

    class Meta:
        model = KnowerUser
        fields = [
            "email",
            "password",
        ]
