
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Questions(models.Model):
    title=models.CharField(max_length=200)
    description=models.CharField(max_length=400)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateField(auto_now_add=True)
    image=models.ImageField(upload_to="images",null=True)

    def __str__(self):
        return self.title


class Answers(models.Model):
    questions=models.ForeignKey(Questions,on_delete=models.CASCADE)
    answers=models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateField(auto_now_add=True)
    up_vote=models.ManyToManyField(User,related_name="up_vote")

    def __str__(self):
        return self.answers




#from orkut.models import Questions,Answes
#from django.contrib.auth.models import User
# usr=User.objects.get(id=2)
#Questions.objects.create(title="django",description="django architecture?",user=usr)
#usr.questions_set.create(title="javascript",description="is js synchronous")
#usr.questions_set.all()
#ques=Questions.objects.get(id=4)
#ques.answers_set.create(answers="qatar",user=usr
#ans=Answers.objects.get(id=4)
# ans.upvote.add(usr)
#ans.up_vote.all() 