from django.db import models

# Create your models here.
class Owner(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False) 
    age = models.IntegerField()
    number_of_pets = models.PositiveBigIntegerField()

class Cat(models.Model):
    breed = models.CharField(max_length=100)
    age = models.PositiveBigIntegerField()
    vaccinated = models.BooleanField(default=True)
    description = models.TextField(max_length=200)
    name = models.CharField(max_length=100)

class Bird(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveBigIntegerField()
    vaccinated = models.BooleanField(default=True)
    description = models.TextField(max_length=200)
    species = models.CharField(max_length=100)

class Dog(models.Model):
    age = models.PositiveBigIntegerField()
    name = models.CharField(max_length=100)
    vaccinated = models.BooleanField(default=True)
    breed = models.CharField(max_length=100)
    description = models.TextField(max_length=200)

class Exotic_Animal(models.Model):
    region_of_origin = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    age = models.PositiveBigIntegerField()
    type_of_animal = models.CharField(max_length=100)
    vaccinated = models.BooleanField(default=True)
        
