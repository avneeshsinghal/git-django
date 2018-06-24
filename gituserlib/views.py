from gituserlib.models import User
from gituserlib.serializers import UserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests


class UserSearch(APIView):
    """
    List all gituserlib, or create a new snippet.
    """
    def get(self, request, format=None):
        username = request.query_params.get("user")
        url = "http://api.github.com/users/"+username
        headers = {
            'Cache-Control': "no-cache"
        }
        user_request = requests.request("GET", url, headers=headers).json()
        print(user_request)

        update_payload = {
            "email": user_request.get("email"),
            "username": user_request.get("login")

        }
        find_by_user = User.objects.filter(username=username)
        if not list(UserSerializer(find_by_user, many=True).data):
            User.objects.create(**update_payload)
            print("yes")
            find_by_user = User.objects.filter(username=username)
        else:
            find_by_user.update(**update_payload)

        return Response(UserSerializer(find_by_user, many=True).data)





    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)