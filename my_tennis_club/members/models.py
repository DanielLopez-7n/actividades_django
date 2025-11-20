from enum import member
from django.db import models



# Create your models here.
class Member(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)
    email = models.EmailField(max_length=254, null=True)
    address = models.CharField(max_length=255, null=True)
    
def __str__(self):
    return f"{self.firstname} {self.lastname}"