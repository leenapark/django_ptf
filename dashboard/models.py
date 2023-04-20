from django.db import models
import datetime

# Create your models here.
class DashData(models.Model):
    regDate = models.DateField()
    restaurant = models.CharField(max_length=300)
    personnel = models.IntegerField()
    price = models.IntegerField()
    borough = models.CharField(max_length=500, default = '')

# class TestData(models.Model):
#     restaurant = models.CharField(max_length=300)
#     psSum = models.IntegerField()
#     prSum = models.IntegerField()