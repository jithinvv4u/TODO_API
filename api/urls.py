from django.urls import path
from .views import ListToDo,loadIndex

urlpatterns = [
    path('',loadIndex),
    path('list/',ListToDo.as_view(),name='todo'),
    path('list/<int:pk>',ListToDo.as_view(),name='todoID'),
    path('create/',ListToDo.as_view()),
    # path('update/<int:pk>',UpdateToDo.as_view()),
    # path('delete/<int:pk>',DeleteToDo.as_view()),
]
