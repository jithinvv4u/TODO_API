from email import message
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from rest_framework.views import View
from .serializers import RegisterSerializer
from rest_framework.permissions import AllowAny

from django.contrib.auth.forms import AuthenticationForm
from .forms import LoginForm
from django.contrib.auth import authenticate,login

def registerPage(request):
    return render(request,'userRegister.html')

# def loginPage(request):
#     form = AuthenticationForm()
#     return render(request,'userLogin.html',{'form':form})

class RegisterView(View):
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
            return JsonResponse({'message':'success...You can login now'})
        print(serialized.errors)
        return JsonResponse({'message':'Error'})
        # form=self.form_class(request.POST)
        # if form.is_valid():
        #     form.save()
        #     print('form ok')
        # print(form.errors())
        # serialized=self.serializer(data=request.data)


class LoginView(View):
    form_class=LoginForm
    
    def get(self,request,*args,**kwrag):
        form=self.form_class
        return render(request,'userLogin.html',{'form':form})
    
    def post(self,request,*args,**kwrags):
        form=self.form_class(request.POST)
        print('ok')
        if form.is_valid():
            user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
            if user is not None:
                form = login(request, user)
                # messages.success(request, f' wecome {username} !!')
                return redirect('index')
        else:
            # messages.info(request, f'account done not exit plz sign in')
            print('not valid')


# from django.shortcuts import render
# from .serializers import RegisterSerializer
# from rest_framework.views import View
# from .forms import RegisterForm
# # Create your views here.



# def registerPage(request):
#     form=RegisterForm()
#     return render(request,'userRegister.html',{'form':form})

# class RegisterUserView(View):
#     serializer= RegisterSerializer
#     form_class=RegisterForm
    
#     def post(self,request,*args,**kwragS):
#         print(request.POST)
#         form=self.form_class(request.POST)
#         if form.is_valid():
#             form.save()
#             print('form ok')
#         print(form.errors())
#         # serialized=self.serializer(data=request.data)
#         pass