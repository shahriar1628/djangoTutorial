from cffi import model
from django.db import models

class Person(models.Model):
    firstName = models.CharField(max_length = 30)
    lastName = models.CharField(max_length=30)

    def __init__(self,data):
        self.firstName = data['firstName']
        self.lastName = data['lastName']





class Section(models.Model):
    sectionName = models.CharField(max_length=30)
    totalcapacity = models.IntegerField()

class student(models.Model):
    rollNumber = models.CharField(max_length = 30)
    meritStatus = models.IntegerField()
    person = models.OneToOneField(Person,on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.PROTECT)



# Create your models here.
