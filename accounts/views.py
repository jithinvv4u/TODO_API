from django.http import JsonResponse
from django.shortcuts import redirect, render
from .serializers import RegisterSerializer
from django.contrib import messages
from .forms import LoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from rest_framework.views import APIView

def registerPage(request):
    return render(request,'userRegister.html')

class RegisterView(APIView):
    serializer_class = RegisterSerializer
    
    def post(self,request,*args,**kwrags):
        data={}
        data['username']=request.POST['username']
        data['email']=request.POST['email']
        data['password']=request.POST['password']
        data['password2']=request.POST['password2']
        serialized=RegisterSerializer(data=data)
        if serialized.is_valid():
            serialized.save()
            return redirect('login')
        return JsonResponse({'message':'Invalid Credential'})
        # form=self.form_class(request.POST)
        # if form.is_valid():
        #     form.save()
        # print(form.errors())
        # serialized=self.serializer(data=request.data)


def LoginView(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
            if user is not None:
                form = login(request, user)
                return redirect('index')
            else:
                messages.error(request,'Account does not exist')
        else:
            messages.error(request,'Fill the Username And Password')
    else:
        form=LoginForm()
    return render(request,'userLogin.html',{'form':form})
    

def user_logout(request):
    logout(request)
    return redirect('index')