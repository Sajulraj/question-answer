
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


class Answes(models.Model):
    questions=models.ForeignKey(Questions,on_delete=models.CASCADE)
    answers=models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateField(auto_now_add=True)
    up_vote=models.ManyToManyField(User,related_name="up_vote")

    def __str__(self):
        return self.answers




