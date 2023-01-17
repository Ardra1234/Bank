from django.db import models


# Create your models here.
class UserDetails(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    age = models.IntegerField()
    ph = models.CharField(max_length=13)
    mailid = models.EmailField(max_length=20)
    usname = models.CharField(max_length=13)
    pawd = models.CharField(max_length=13)
    status = models.CharField(max_length=10, default='active')