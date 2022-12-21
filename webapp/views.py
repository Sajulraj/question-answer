from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView,CreateView,FormView,ListView
from webapp.form import UserRegistrationForm,UserLoginForm,QuestiionForm
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
            messages.success(request,"You must login first")
            return redirect("signin")
        else:
            return fn(request,*args,**kw)
    return wrapper

class RegistrationView(CreateView):
    template_name="register.html"
    form_class=UserRegistrationForm
    model=User
    success_url=reverse_lazy("signin")
    def form_valid(self, form):
        messages.success(request,"Login successfull")
        return super().form_valid(form)
   
    

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
class IndexView(CreateView,ListView):
    template_name="index.html"
    form_class=QuestiionForm
    success_url=reverse_lazy("home")
    model=Questions
    context_object_name="questions"

    def form_valid(self, form):
        form.instance.user=self.request.user
        messages.success(self.request,"your question added successfully")
        return super().form_valid(form)
    def get_queryset(self):

        return Questions.objects.exclude(user=self.request.user).order_by("-created_date")
