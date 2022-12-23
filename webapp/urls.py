from django.urls import path
from webapp.views import RegistrationView,LoginView,IndexView,add_answer,answer_upvote_view,signout_view

urlpatterns=[
    path("register",RegistrationView.as_view(),name="register"),
    path("",LoginView.as_view(),name="signin"),
    path("index",IndexView.as_view(),name="home"),
    path("questions/<int:id>/answers/add",add_answer,name="add-answer"),
    path("answers/<int:id>/upvote/add",answer_upvote_view,name="add-upvote"),
    path("logout",signout_view,name="sign-out")
]