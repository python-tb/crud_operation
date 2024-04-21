from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=35)
    age = models.IntegerField()
    course = models.CharField(max_length=30)
    address = models.TextField()
    

    def __str__(self):
        return self.name 


