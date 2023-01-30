from django.db import models

# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=60)
    price = models.PositiveIntegerField()
    discount = models.PositiveIntegerField()
    duration = models.CharField(max_length=30)
    author_name = models.CharField(max_length=30)
    def __str__(self):
        return self.name