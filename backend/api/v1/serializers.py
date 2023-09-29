from rest_framework import serializers

from users.models import User


class UsersCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for processing queries about the list of users,
    an individual user and user registration.
    """
    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "username",
            "first_name",
            "last_name",
            "password",
        )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Function for creating a user."""
        user = User.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
