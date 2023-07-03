from rest_framework import serializers
from user.serializers import UserSerializer
from finalapp.models import User


class RegisterSerializer(UserSerializer):
    # id = serializers.UUIDField(source='public_id', read_only=True, format='hex')
    password = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email',
                  'height', 'weight', 'gender', 'dob', 'profile_image', 'is_active','created','updated', 'password']
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)