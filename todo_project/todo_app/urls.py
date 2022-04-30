from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('users/', views.UserViewSet.as_view({'get': 'retrieve'})),
    path('users/<int:my_id>/', views.IdUserAPIView.as_view(), name="user"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/me', views.UserAPI.as_view()),

]
