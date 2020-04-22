from django.db import models

# Create your models here.


class Employee(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    empid = models.CharField(max_length=30)

    def __str__(self):
        return self.firstname
