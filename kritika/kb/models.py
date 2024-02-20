from django.db import models
class userinfo(models.Model):
    username = models.TextField(max_length=100,default='username') 
    number = models.IntegerField(null=True,blank=True)
    email = models.CharField(max_length=100)
    password = models.TextField(default='password')
    confirm_password = models.TextField(default='password')
   
# class UserInfo
