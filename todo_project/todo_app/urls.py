from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
<<<<<<< Updated upstream
    path('users/', views.UserAPIView.as_view())

=======
    path('users/', views.UserViewSet.as_view({'get': 'retrieve'})),
    path('users/<int:id>', views.dynamic_lookup_view, name="user")
>>>>>>> Stashed changes
]
