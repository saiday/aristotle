from django.contrib.auth.models import Group
from rest_framework import serializers

from aristotle.models import Ticket
from locations.models import Location, City
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


class TicketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = City
        fields = '__all__'
