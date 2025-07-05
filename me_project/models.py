from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class ContactInfo(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=50)
    phone = PhoneNumberField(max_length= 20)
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=255)

    def __str__(self):
        return self.name
