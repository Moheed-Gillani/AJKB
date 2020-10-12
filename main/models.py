from django.db import models
from django.contrib.auth.models import User

class Profiles(models.Model):
    User=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    Name=models.CharField(max_length=10,blank=True)
    Image=models.ImageField(null=True)
    def __str__(self):
        return str(self.Name)

# Create Profiles Posts here.
class Post(models.Model):
    posted_by=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    image=models.ImageField(null=True)
    headline=models.CharField(max_length=200)
    text=models.TextField()
    date=models.DateField(auto_created=True,null=True)
    def __str__(self):
        return self.headline

# Create Profiles models here.
class Comment(models.Model):
    on_post=models.ForeignKey(Post,on_delete=models.CASCADE)
    comment=models.TextField()
    name=models.ForeignKey(Profiles,on_delete=models.CASCADE,null=True)
    on=models.DateField(null=True,auto_now=True)
    def __str__(self):
        return self.comment
class Reply(models.Model):
    on_comment=models.ForeignKey(Comment,on_delete=models.CASCADE)
    Reply=models.TextField()
    name=models.ForeignKey(Profiles,on_delete=models.CASCADE,null=True)
    on=models.DateField(null=True,auto_now=True)
    def __str__(self):
        return self.Reply





