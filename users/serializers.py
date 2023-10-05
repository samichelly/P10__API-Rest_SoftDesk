from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from datetime import date


CustomUser = get_user_model()


class SignupSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )

    date_of_birth = serializers.DateField(required=True)
    can_be_contacted = serializers.BooleanField(required=True)
    can_data_be_shared = serializers.BooleanField(required=True)

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "password",
            "password2",
            "date_of_birth",
            "can_be_contacted",
            "can_data_be_shared",
        )

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields did not match."}
            )

        date_of_birth = attrs["date_of_birth"]
        today = date.today()
        age = (
            today.year
            - date_of_birth.year
            - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
        )

        if age < 15:
            raise serializers.ValidationError(
                {"date_of_birth": "You must be at least 15 years old to register."}
            )

        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            date_of_birth=validated_data["date_of_birth"],
            can_be_contacted=validated_data["can_be_contacted"],
            can_data_be_shared=validated_data["can_data_be_shared"],
        )
        user.set_password(validated_data["password"])
        user.save()

        return user
