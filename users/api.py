from rest_framework import generics
from rest_framework.response import Response
from .serializer import UserSerializer
from django.contrib.auth.models import User

class UserApi(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer