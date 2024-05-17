from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import FileField, Serializer


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class UploadSerializer(Serializer):
    file_uploaded = FileField()

    class Meta:
        fields = ["file_uploaded"]
