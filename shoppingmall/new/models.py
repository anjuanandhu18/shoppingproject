from django.db import models

# Create your models here.
class registerTable(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    mobile=models.CharField(max_length=30)
    adress= models.CharField(max_length=20)