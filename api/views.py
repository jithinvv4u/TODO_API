from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.http import Http404,QueryDict
from .models import ToDo
from .serializers import ToDoSerializer


def loadIndex(request):
    return render(request,'index.html')

class ListToDo(View):
    serializer=ToDoSerializer
    model=ToDo
    
    def get_object(self, pk):
        try:
            return self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            raise Http404

    def get(self,request,*args,**kwrags):
        queryset=self.model.objects.all().order_by('-created_at')
        serialized=self.serializer(queryset,many=True)
        return JsonResponse({'data':serialized.data})
        
    def post(self,request,*args,**kwrags):
        data={'title':request.POST.get('title'),'completed':False}
        serialized=self.serializer(data=data)
        if serialized.is_valid():
            serialized.save()
        return JsonResponse(serialized.data)
    
    def put(self,request,pk,*args,**kwrags):
        queryset=self.get_object(pk)
        title=QueryDict(request.body).get('title')
        data={'id':pk,'title':title,}
        serialized=self.serializer(queryset,data=data)
        if serialized.is_valid():
            serialized.save()
            return JsonResponse(serialized.data)
        return Response(serialized.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk,*arg,**kwrags):
        queryset=self.get_object(pk)
        checkData=self.model.objects.filter(pk=pk).values('completed')
        
        if checkData[0]['completed']==False:
            data={'completed':True}
            serialized=self.serializer(queryset,data=data,partial=True)
            if serialized.is_valid():
                serialized.save()
        elif checkData[0]['completed']==True:
            data={'completed':False}
            serialized=self.serializer(queryset,data=data,partial=True)
            if serialized.is_valid():
                serialized.save()
        return JsonResponse(serialized.data)
    
    def delete(self,request,pk,*arg,**kwrags):
        datas=self.get_object(pk)
        datas.delete()
        return JsonResponse({'data':pk})
   
   
   
   
    
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

    
# @api_view(['POST'])
# def createToDo(requset):
#     title=requset.POST.get('title')
#     data={'title':'title','description':'des'}
#     serializer=ToDoSerializer(data=data)
#     if serializer.is_valid():
#         print('ok')
#     print('not working')
#     print(serializer.errors)
    
#     return Response(serializer.data)