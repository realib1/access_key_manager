from rest_framework import serializers
from key_manager.models import AccessKey


class AccessKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessKey
        fields = '__all__'