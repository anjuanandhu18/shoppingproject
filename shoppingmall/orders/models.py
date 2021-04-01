from django.db import models

# Create your models here.
class Details(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    adress=models.TextField(max_length=300)

class Mark(models.Model):
    subject=models.CharField(max_length=20)
    mark=models.IntegerField()
    status=models.CharField(max_length=30)
    specialid=models.IntegerField(unique=True)