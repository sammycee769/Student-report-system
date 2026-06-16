from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainSerializer
from rest_framework_simplejwt.tokens import RefreshToken


class StudentEnrollmentSerializers(serializers.Serializer):
    department = serializers.CharField(max_length=10, required=True)
    entry_year = serializers.IntegerField()
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True,write_only=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

class StaffRegistrationSerializers(serializers.Serializer):
    department = serializers.CharField(max_length=10, required=True)
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True,write_only=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

class CustomTokenObtainSerializer(TokenObtainSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True,write_only=True)

    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user
        refresh = RefreshToken.for_user(user)

        data["user"] = {
            "id": user.id,
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "email": user.email,
            "username": user.username,
            "role" : user.role,
        }
        return data
