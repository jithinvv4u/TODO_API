from django.urls import path
from .views import ListToDo,loadIndex

urlpatterns = [
    path('',loadIndex,name='index'),
    path('list/',ListToDo.as_view(),name='todo'),
    path('list/<int:pk>',ListToDo.as_view(),name='todoID'),
]
