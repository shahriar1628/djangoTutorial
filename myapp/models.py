from cffi import model
from django.db import models

class Person(models.Model):
    firstName = models.CharField(max_length = 30)
    lastName = models.CharField(max_length=30)
    picture = models.ImageField(upload_to='pictures/',null=True)


    @classmethod
    def create(cls, firstName,lastName,picture):
        person = cls(firstName = firstName, lastName = lastName,picture=picture)
        return person




class Book(models.Model):
    title = models.CharField(max_length=100)

    @classmethod
    def create(cls, title):
        book = cls(title=title)
        # do something with the book
        return book


class Section(models.Model):
    sectionName = models.CharField(max_length=30)
    totalcapacity = models.IntegerField()

class student(models.Model):
    rollNumber = models.CharField(max_length = 30)
    meritStatus = models.IntegerField()
    person = models.OneToOneField(Person,on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.PROTECT)



# Create your models here.
