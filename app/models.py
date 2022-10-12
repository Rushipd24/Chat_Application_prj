from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

user_status_choices = [('Active','Active'),('Inactive','Inactive')]
class User(AbstractUser):
    user_id       =  models.AutoField(primary_key=True)
    email         =  models.EmailField(max_length=254,null=True, blank=True,unique=True)
    phone         =  models.CharField(max_length=12,null=True, blank=True)
    Status        =  models.CharField(max_length=10, choices=user_status_choices, default='Active')
    created_date  =  models.DateTimeField(auto_now_add=True)
    modified_date =  models.DateTimeField(auto_now=True)
    created_by    =  models.CharField(max_length=100, blank=True,null=True)
    modified_by   =  models.CharField(max_length=100, blank=True, null=True)

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['username',]

    def __str__(self) -> str:
        return self.username


class Group(models.Model):
    grp_id        =  models.AutoField(primary_key=True)
    grp_name      =  models.EmailField(max_length=254,null=True, blank=True,unique=True)
    Status        =  models.CharField(max_length=10, choices=user_status_choices, default='Active')
    created_date  =  models.DateTimeField(auto_now_add=True)
    modified_date =  models.DateTimeField(auto_now=True)
    created_by    =  models.CharField(max_length=100, blank=True,null=True)
    modified_by   =  models.CharField(max_length=100, blank=True, null=True)

    
class Message(models.Model):
    msg_id        =  models.AutoField(primary_key=True)
    msg_desc      =  models.EmailField(max_length=254,null=True, blank=True)
    msg_for       =  models.ForeignKey(User, on_delete=models.CASCADE)  
    Status        =  models.CharField(max_length=10, choices=user_status_choices, default='Active')
    created_date  =  models.DateTimeField(auto_now_add=True)
    modified_date =  models.DateTimeField(auto_now=True)
    created_by    =  models.CharField(max_length=100, blank=True,null=True)
    modified_by   =  models.CharField(max_length=100, blank=True, null=True)
