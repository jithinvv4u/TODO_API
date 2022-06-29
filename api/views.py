from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics,mixins
from .models import ToDo
from .serializers import ToDoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views import View
# Create your views here.
def loadIndex(request):
    return render(request,'index.html')
# class ListToDo(generics.ListAPIView):
#     serializer_class=ToDoSerializer
#     queryset=ToDo.objects.all()

# class CreateToDo(generics.CreateAPIView):
#     serializer_class=ToDoSerializer
#     queryset=ToDo.objects.all()

# class UpdateToDo(generics.RetrieveUpdateAPIView):
#     serializer_class=ToDoSerializer
#     queryset=ToDo.objects.all()
    
# class DeleteToDo(generics.DestroyAPIView):
#     serializer_class=ToDoSerializer
#     queryset=ToDo.objects.all()
    
# @api_view(['GET'])
# def listToDo(request):
#     tasks=ToDo.objects.all()
#     serializer=ToDoSerializer(tasks,many=True)
#     return Response(serializer.data)

class ListToDo(View):
    serializer=ToDoSerializer
    model=ToDo
    
    def get(self,request,*args,**kwrags):
        datas=self.model.objects.all().order_by('-created_at')
        serialized=self.serializer(datas,many=True)
        return JsonResponse({'data':serialized.data})
        
    def post(self,request,*args,**kwrags):
        data={}
        data['title']=request.POST.get('title')
        serialized=self.serializer(data=data)
        if serialized.is_valid():
            serialized.save()
        return JsonResponse(data)
    
    def put(self,request,*args,**kwrags):
        pass
    
    def delete(self,request,*arg,**kwrags):
        pass
        
@api_view(['POST'])
def createToDo(requset):
    title=requset.POST.get('title')
    data={'title':'title','description':'des'}
    serializer=ToDoSerializer(data=data)
    if serializer.is_valid():
        print('ok')
    print('not working')
    print(serializer.errors)
    
    return Response(serializer.data)