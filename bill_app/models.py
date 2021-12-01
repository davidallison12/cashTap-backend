from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import BooleanField
import phonenumbers
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = PhoneNumberField()
    email_reminder = BooleanField(default=False)
    text_reminder = BooleanField(default=False)
    
    def __str__(self):
        return self.user



class Bill (models.Model):
    bill_type = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100, default='Company Name')
    bill_due_date = models.CharField(max_length=100)
    min_payment = models.DecimalField(max_digits=7, decimal_places=2)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, default={})

    def __str__(self):
        return self.company_name