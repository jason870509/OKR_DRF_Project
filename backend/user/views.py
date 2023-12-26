from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .serializers import UserSerializer
from reports.permissions import IsStaffEditorPermission


# Create your views here.
class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = []

    def perform_create(self, serializer):
        print(serializer.validated_data)

        username = serializer.validated_data.get('username')

        
        if User.objects.filter(username=username).exists():
            return Response({"message": "That username is taken"})
        else:
            serializer.validated_data['is_staff'] = True

        user = User.objects.create_user(**serializer.validated_data)
        user.save()

        # serializer.save()


user_create_view = UserCreateAPIView.as_view()