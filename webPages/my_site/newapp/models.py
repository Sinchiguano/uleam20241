from django.db import models

# Create your models here.
from django.db import models 
class Person(models.Model): 
    person_name = models.CharField(max_length=20) 
    email = models.EmailField() 
    phone = models.CharField(max_length=20) 
    age = models.IntegerField(default=18,null=True, blank=True)
