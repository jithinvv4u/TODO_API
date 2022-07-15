from django.urls import path
from .views import LoginView, RegisterView, registerPage
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('',registerPage),
    path('register/',RegisterView.as_view(),name='user_register'),
    path('login/',LoginView.as_view(),name='login'),
    path(r'logout/$',auth_view.LogoutView,name='logout'),
]
