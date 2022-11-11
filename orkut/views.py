from django.shortcuts import render
from .serializers import UserSerializer,QuestionSerializer,Answerserializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Questions,Answers
from rest_framework import authentication,permissions
from rest_framework.decorators import action
# Create your views here.

class OrkutModelview(ModelViewSet):
    serializer_class=UserSerializer
    queryset=User.objects.all()

class QuestionViewset(ModelViewSet):
    serializer_class=QuestionSerializer
    queryset=Questions.objects.all()
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):
          serializer.save(user=self.request.user)
    @action(methods=["get"],detail=False)
    def my_question(self,request,*args,**kw):
        qs=request.user.questions_set.all()
        serializer=QuestionSerializer(qs,many=True)
        return Response(data=serializer.data)
    @action(methods=["post"],detail=True)
    def add_answer(self,request,*args,**kw):
        id=kw.get("pk")
        ques=Questions.objects.get(id=id)
        usr=request.user
        sr=Answerserializer(data=request.data,context={"user":usr,"question":ques})
        if sr.is_valid():
            sr.save()
            return Response(data=sr.data)
        else:
            return Response(data=sr.errors)
    @action(methods=["get"],detail=True)
    def list_answer(self,request,*args,**kw):
        id=kw.get("pk")
        ques=Questions.objects.get(id=id)
        qs=ques.answers_set.all()
        serializer=Answerserializer(qs,many=True)
        return Response(data=serializer.data)



class AnswerViewset(ModelViewSet):
    serializer_class=Answerserializer
    queryset=Answers.objects.all()
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    @action(methods=["get"],detail=True)
    def up_vote(self,request,*args,**kw):
        ans=self.get_object()
        usr=request.user
        ans.up_vote.add(usr)
        return Response(data="upvoted")