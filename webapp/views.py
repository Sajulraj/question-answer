from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView
from webapp.form import UserRegistrationForm,UserLoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login


# Create your views here.

class RegistrationView(View):
    def get(self,request,*args,**kw):
        form=UserRegistrationForm()
        return render(request,"register.html",{"form":form})

    def post(self,request,*args,**kw):
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            return redirect("register")
        else:
            return render(request,"register.html",{"form":form})


class LoginView(View):
    def get(self,request,*args,**kw):
        form=UserLoginForm()
        return render(request,"login.html",{"form":form})
