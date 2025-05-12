from django.db import models

# Create your models here.
class Farmer(models.Model):
    name = models.CharField(max_length=200)
    farm_name = models.CharField(max_length=150)

class Buyer(models.Model):
    name = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)

class Driver(models.Model):
    name = models.CharField(max_length=200)
    truck_plate_number = models.IntegerField()