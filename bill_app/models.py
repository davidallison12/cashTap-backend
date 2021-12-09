from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import BooleanField
import phonenumbers
from phonenumber_field.modelfields import PhoneNumberField

# Built in signal for post_save (To extend User)
from django.db.models.signals import post_save
# Decorator with Signal receiver 
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = PhoneNumberField()
    email_reminder = BooleanField(default=False)
    text_reminder = BooleanField(default=False)
    
    def __str__(self):
        return self.user


# receiver function called when new User instance  is creted 
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


#  receiver function called when User instance is updated
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



class Bill (models.Model):
    MEDICAL = 'medical'
    UTILITIES = 'utilities'
    CABLE_INTERNET = 'cable/internet'
    SUBSCRIPTION = 'subscription'
    PHONE = 'phone'
    CREDIT_CARD = 'credit card'
    INSURANCE = 'insurance'

    BILL_TYPES = [
        (MEDICAL, 'medical'),
        (UTILITIES, 'utilities'),
        (CABLE_INTERNET, 'cable/internet'),
        (SUBSCRIPTION, 'subscription'),
        (PHONE, 'phone'),
        (CREDIT_CARD, 'credit card'),
        (INSURANCE, 'insurance'),
    ]


    bill_type = models.CharField(max_length=100, choices=BILL_TYPES, default=CREDIT_CARD)
    company_name = models.CharField(max_length=100, default='Company Name')
    bill_due_date = models.DateField(auto_now=False, auto_now_add=False)
    min_payment = models.DecimalField(max_digits=7, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.company_name
