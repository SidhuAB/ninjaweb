from django.db import models

# Create your models here.
class login(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=250,null=True, blank=True)
    password = models.CharField(max_length=100)
    
    