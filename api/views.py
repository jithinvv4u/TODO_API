from django.shortcuts import render
from rest_framework import generics
from .models import ToDo
from .serializers import ToDoSerializer
# Create your views here.

class ListToDo(generics.ListAPIView):
    serializer_class=ToDoSerializer
    queryset=ToDo.objects.all()

class CreateToDo(generics.CreateAPIView):
    serializer_class=ToDoSerializer
    queryset=ToDo.objects.all()

class UpdateToDo(generics.RetrieveUpdateAPIView):
    serializer_class=ToDoSerializer
    queryset=ToDo.objects.all()
    
class DeleteToDo(generics.DestroyAPIView):
    serializer_class=ToDoSerializer
    queryset=ToDo.objects.all()