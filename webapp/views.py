from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView,CreateView,FormView
from webapp.form import UserRegistrationForm,UserLoginForm,QuestionForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from orkut.models import Questions
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib import messages

# Create your views here.
def signin_required(fn):
    def wrapper(request,*args,**kw):
        if not request.user.is_authenticated:
            messages.error(request,"You must login first")
            return redirect("signin")
        else:
            return fn(request,*args,**kw)
    return wrapper

class RegistrationView(CreateView):
    template_name="register.html"
    form_class=UserRegistrationForm
    model=User
    success_url=reverse_lazy("signin")
   
    

class LoginView(FormView):
    template_name="login.html"
    form_class=UserLoginForm

    def post(self,request,*args,**kw):
        form=UserLoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                messages.success(request,"Login successfull")
                return redirect("home")
            else:
                print("invalid user")
                messages.success(request,"Invalid user")
                return render("signin")

@method_decorator(signin_required,name="dispatch")
class IndexView(TemplateView):
    template_name="index.html"

class QuestionLstView(View):
    def get(self,request,*args,**kw):
        qs=Questions.objects.filter(user=request.user)
        return render(request,"question-list.html",{"question":qs})