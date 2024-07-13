from rest_framework import generics
from key_manager.models import AccessKey
from .serializers import AccessKeySerializer
from rest_framework.permissions import IsAuthenticated


class AccessKeyListCreate(generics.ListCreateAPIView):
    queryset = AccessKey.objects.all()
    serializer_class = AccessKeySerializer
    permission_classes = [IsAuthenticated]
