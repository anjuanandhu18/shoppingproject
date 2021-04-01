from django.db import models


# Create your models here.
class FirstTable(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    number=models.IntegerField(blank=True,null=True)

