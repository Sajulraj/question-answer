from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Questions,Answers

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields=["email","username","password"]
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class Answerserializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    questions=serializers.CharField(read_only=True)
    created_date=serializers.CharField(read_only=True)
    upvotes=serializers.CharField(read_only=True)
    class Meta:
        model=Answers
        fields=[
            "id","questions","answers","user","created_date", "upvotes"
            ]

    def create(self, validated_data):
        Usr=self.context.get("user")
        ques=self.context.get("question")
        return ques.answers_set.create(user=Usr,**validated_data)


class QuestionSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    question_answers=Answerserializer(read_only=True,many=True)
   
    class Meta:
        model=Questions
        fields=[
                "id",
                 "title",
                 "description",
                 "image",
                "user",
                "question_answers",
                
                ]