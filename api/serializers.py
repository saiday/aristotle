from django.contrib.auth.models import Group
from rest_framework import serializers

from users.models import CustomUser


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('url', 'email', 'is_staff', 'account_name')

    def validate_account_name(self, value):
        if ' ' in value:
            raise serializers.ValidationError("account_name contains white space, this is not allowed")
        return value


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
