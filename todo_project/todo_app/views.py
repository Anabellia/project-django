from asyncio import run_coroutine_threadsafe
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, generics
from django.shortcuts import render
from .serializers import UserSerializer, UserAPISerializer, NameUserSerializer
from todo_app.models import MyUser, NameFieldForUser
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, IsAdminUser, BasePermission
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin


class UserList(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = MyUser.objects.all()
        name = self.request.query_params.get('name')

        if name is not None:
            queryset = queryset.filter(
                first_name=name) | queryset.filter(
                last_name=name)

        return queryset


# class UserList(generics.ListAPIView):
#     serializer_class = UserSerializer

#     def get_queryset(self):
#         queryset = MyUser.objects.all()
#         first_name = self.request.query_params.get('first_name')
#         last_name = self.request.query_params.get('last_name')

#         if first_name is not None:
#             queryset = queryset.filter(
#                 first_name=first_name)
#         if last_name is not None:
#             queryset = queryset.filter(
#                 last_name=last_name)

#         return queryset


class UserReadPermission(BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser


class UserAPI(APIView):
    permission_classes = [IsAuthenticated]
    serizalizer_class = UserSerializer

    def get_object(self):
        return self.request.user

    def get(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = UserSerializer(user)
        return Response(serializer.data)


# class IdUserAPIView(APIView):

#     def get(self, request, my_id, *args, **kwargs):
#         if self.request.user.is_superuser:
#             user = MyUser.objects.get(id=my_id)
#             serializer = UserSerializer(user)
#             return Response(serializer.data)
#         else:
#             return Response({"detail": "Only admin is allowed see this resource"})

class IdUserAPIView(viewsets.GenericViewSet, RetrieveModelMixin):
    permission_classes = [UserReadPermission]
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer

    # def retrieve(self, request, my_id):
    #     user = self.get_object()
    #     print(user)
    #     # user = MyUser.objects.get(id=my_id)
    #     # serializer = UserSerializer(user)
    #     return Response()


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
