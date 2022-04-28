from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('users/', views.UserViewSet.as_view({'get': 'retrieve'})),
]
