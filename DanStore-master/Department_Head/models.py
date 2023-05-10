from django.db import models
from Store_manager.models import *


class dept_request_form1(models.Model):
    request_store=models.ForeignKey(allStore,null=True,blank=True,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True,null=True)
    Request_by=models.CharField(max_length=100,null=True,blank=True)
    Department=models.CharField(max_length=100,null=True,blank=True)
    checkd_by=models.ForeignKey(employ,null=True,blank=True,on_delete=models.CASCADE) 
class dept_request_form2(models.Model):
    dept_request_form1=models.ForeignKey(dept_request_form1,null=True,blank=True,on_delete=models.CASCADE)
    Description=models.CharField(max_length=100,null=True,blank=True)
    unit=models.CharField(max_length=100,null=True,blank=True)
    req_qty=models.CharField(max_length=100,null=True,blank=True)
    Remark=models.CharField(max_length=100,null=True,blank=True)


class dept_request_form1_permanent(models.Model):
    store_Keeper_action_choice=(
        ('Pending','Pending'),
        ('Allowed','Allowed'),
        ('wait','wait'),
        ('Reject','Reject'),
    )
    dept_head_action_choice=(
        ('Pending','Pending'),
        ('Approved','Approved'),
        ('Rejected','Rejected'),
    )
    Recival_status=(
        ('Received ','Received'),
        ('Not_Received ','Not_Received'),
         ('Returned','Returned'),
    )
    Recival_status_by_Employer=models.CharField(max_length=200,null=True,choices=Recival_status)
    request_store=models.ForeignKey(allStore,null=True,blank=True,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True,null=True)
    dept_head_Action=models.CharField(max_length=200,null=True,choices=dept_head_action_choice,default='Approved')
    Store_Keeper_Action=models.CharField(max_length=200,null=True,choices=store_Keeper_action_choice,default='Pending')
    Request_by=models.CharField(max_length=100,null=True,blank=True)
    Department=models.CharField(max_length=100,null=True,blank=True)
    checkd_by=models.ForeignKey(employ,null=True,blank=True,on_delete=models.CASCADE)
    Description=models.CharField(max_length=100,null=True,blank=True)
    unit=models.CharField(max_length=100,null=True,blank=True)
    req_qty=models.CharField(max_length=100,null=True,blank=True)
    Remark=models.CharField(max_length=100,null=True,blank=True)
    note=models.TextField(max_length=100,null=True,blank=True)
    Type_of_item=models.TextField(max_length=100,null=True,blank=True)
    Serial_No=models.TextField(max_length=100,null=True,blank=True)
    Unique_Name_No=models.TextField(max_length=100,null=True,blank=True)
# Create your models here.
