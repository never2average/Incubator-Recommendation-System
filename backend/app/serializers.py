from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class ContactUsSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    subject = serializers.CharField(max_length=200)
    message = serializers.CharField()

class GenerateResultsSerializer(serializers.Serializer):
    profile = serializers.CharField()
    companies = serializers.JSONField(False, None)