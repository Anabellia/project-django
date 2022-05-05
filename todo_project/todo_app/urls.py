from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'myusers', views.IdUserAPIView)

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('users/', views.UserViewSet.as_view({'get': 'retrieve'})),
    #path('users/<int:my_id>/', views.IdUserAPIView.as_view(), name="user"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/me', views.UserAPI.as_view()),
    path('name', views.UserList.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls))

]
