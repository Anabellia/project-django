from asyncio import run_coroutine_threadsafe
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from django.shortcuts import render
from .serializers import UserSerializer, UserAPISerializer
from todo_app.models import MyUser
from rest_framework.permissions import IsAuthenticated


class UserAPI(APIView):
    permission_classes = [IsAuthenticated]
    serizalizer_class = UserSerializer

    def get_object(self):
        return self.request.user

    def get(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = UserSerializer(user)
        return Response(serializer.data)


class IdUserAPIView(APIView):

    def get(self, request, my_id, *args, **kwargs):
        if self.request.user.is_superuser:
            user = MyUser.objects.get(id=my_id)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        else:
            return Response({"Error Admin": "You don't have permission to see this page"})


class UserViewSet(viewsets.ViewSet):

    def retrieve(self, request, *args, **kwargs):
        users = MyUser.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class HomeView(APIView):

    def get(self, request, *args, **kwargs):
        return render(request, 'home.html', {})


# class UserAPIView(APIView):

#     def get_object(self):
#         users = User.objects.all()
#         return users

#     def get(self, request, *args, **kwargs):
#         users = self.get_object()
#         serializer = UserSerializer(users, many=True)

#         return Response(serializer.data)
