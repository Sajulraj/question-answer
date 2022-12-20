from django.urls import path
from webapp import views

urlpatterns=[
    path("register",views.RegistrationView.as_view(),name="register"),
    path("login",views.LoginView.as_view(),name="signin"),
    path("index",views.IndexView.as_view(),name="home"),
    path("question/all",views.QuestionLstView.as_view(),name="question-list")
]