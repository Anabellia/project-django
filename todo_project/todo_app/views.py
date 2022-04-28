from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from .serializers import UserSerializer
from todo_app.models import User


<<<<<<< Updated upstream
=======
def dynamic_lookup_view(request, id):
    obj = User.objects.get(id=1)
    context = {
        "object": obj
    }
    return(request, "user.html", context)


class UserViewSet(viewsets.ViewSet):

    def retrieve(self, request, *args, **kwargs):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


>>>>>>> Stashed changes
class HomeView(APIView):

    def get(self, request, *args, **kwargs):
        return render(request, 'home.html', {})


class UserAPIView(APIView):
    serializer_user = UserSerializer

    def get_object(self):
        users = User.objects.all()
        return users

    def get(self, request, *args, **kwargs):
        users = self.get_object()
        serializer = UserSerializer(users, many=True)

        return Response(serializer.data)
