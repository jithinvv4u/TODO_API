from django.urls import path
from .views import ListToDo,CreateToDo,UpdateToDo,DeleteToDo

urlpatterns = [
    path('list/',ListToDo.as_view()),
    path('create/',CreateToDo.as_view()),
    path('update/<int:pk>',UpdateToDo.as_view()),
    path('delete/<int:pk>',DeleteToDo.as_view()),
]