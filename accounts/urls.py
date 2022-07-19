from django.urls import path
from .views import LoginView, RegisterView, registerPage, user_logout
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('',registerPage,name='signup'),
    path('register/',RegisterView.as_view(),name='user_register'),
    path('login/',LoginView,name='login'),
    path('logout/',user_logout,name='logout'),
    
]
