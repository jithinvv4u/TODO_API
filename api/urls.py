from django.urls import path
from .views import ListToDo,loadIndex,createToDo

urlpatterns = [
    path('',loadIndex),
    path('list/',ListToDo.as_view(),name='todo'),
    path('create/',createToDo),
    # path('update/<int:pk>',UpdateToDo.as_view()),
    # path('delete/<int:pk>',DeleteToDo.as_view()),
]
