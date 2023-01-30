from django.db import models

# Create your models here.


class Cloth(models.Model):
    name = models.CharField(max_length=60)
    price = models.PositiveIntegerField()
    discount = models.PositiveIntegerField()

    def __str__(self):
        return self.name