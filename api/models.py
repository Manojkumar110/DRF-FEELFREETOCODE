from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=20)
    phone = models.IntegerField()
    Natioanlity = models.CharField(max_length=50)

