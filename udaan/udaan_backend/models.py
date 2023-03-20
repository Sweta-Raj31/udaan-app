from django.db import models
import datetime

# Create your models here.
class Message(models.Model):
    name=models.CharField(max_length=255,blank=True,null=True)
    email=models.EmailField(null=True,blank=True)
    subject=models.TextField(blank=True,null=True)
    message=models.TextField(blank=True,null=True)
    date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return (f'{self.name} | {self.subject} | {self.date}')  
    
class Content(models.Model):
    
    name = models.CharField(max_length=255,blank=True,null=True)
   
    email = models.EmailField(null=True,blank=True)
   
    type_content= models.CharField(max_length=255,blank=True,null=True)
    contact = models.BigIntegerField(blank=True,null=True)
    dept= models.CharField(max_length=255,blank=True,null=True)
    college=models.CharField(max_length=225,default='college name')
    content = models.FileField(upload_to='media/', null=True, blank=True)
    
    def __str__(self):
        return (f'{self.name} | {self.type_content}')
    
    
    
