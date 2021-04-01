from django.db import models
from django.db.models import Model


# Create your models here.

class emailModel(Model):
    email_field = models.EmailField(max_length=254)