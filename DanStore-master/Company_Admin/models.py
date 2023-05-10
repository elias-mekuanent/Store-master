from django.db import models
from django.contrib.auth.models import User

class Admin(models.Model):
    user=models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    Full_Name=models.CharField(max_length=300, null=True)
    phone1 = models.CharField(max_length=200, null=True)
    phone2 = models.CharField(max_length=200, null=True)
    facebook = models.CharField(max_length=200, null=True,blank=True)
    telegram = models.CharField(max_length=200, null=True,blank=True)
    instagram = models.CharField(max_length=200, null=True,blank=True)
    about = models.TextField(max_length=500, null=True)
    profile_pic=models.ImageField(null=True,blank=True, upload_to='Profile/')
    Company = models.CharField(max_length=200, null=True)
    Job = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return str(self.user)

class Store_manager(models.Model):
    user=models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    Full_Name=models.CharField(max_length=300, null=True)
    phone1 = models.CharField(max_length=200, null=True)
    phone2 = models.CharField(max_length=200, null=True)
    facebook = models.CharField(max_length=200, null=True,blank=True)
    telegram = models.CharField(max_length=200, null=True,blank=True)
    instagram = models.CharField(max_length=200, null=True,blank=True)
    about = models.TextField(max_length=500, null=True)
    profile_pic=models.ImageField(null=True,blank=True, upload_to='Profile/')
    Company = models.CharField(max_length=200, null=True)
    Job = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return str(self.user)
    
