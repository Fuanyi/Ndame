from rest_framework import serializers
from finalapp.models import User

class UserSerializer(serializers.ModelSerializer):
    # id = serializers.UUIDField(source='public_id', read_only=True, format='hex')
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)

    class Meta:
        model = User
        fields = [ 'username', 'first_name', 'last_name', 'email','password',
                  'height', 'weight', 'gender', 'dob', 'profile_image', 'is_active','created','updated',]
        read_only_fields = ['is_active']

    def update(self, instance, validated_data):
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        instance.save()
        return instance