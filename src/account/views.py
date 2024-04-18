from django.shortcuts import render
from rest_framework import generics
from account.serializers import RegisterSerializer, UserSerializer
from rest_framework.response import Response


class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user_data = UserSerializer(
            user, context=self.get_serializer_context()
        )
        
        user = user_data.data
        return Response(
            {
            "user": user,
            "message": "User Created Successfully.  Now perform Login to get your token",
            }
        )