from django.db import models

class Person(models.Model):
    firstName = models.CharField(max_length = 30)
    lastName = models.CharField(max_length=30)

# Create your models here.
