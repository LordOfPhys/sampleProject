from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Employee(models.Model):
    name = models.CharField(max_length=100, default='name')
    phone_number = models.CharField(max_length=20)