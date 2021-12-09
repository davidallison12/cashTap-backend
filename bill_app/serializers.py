from .models import User, Bill
from rest_framework import serializers 


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ('id', 'bill_type', 'company_name', 'bill_due_date', 'min_payment', 'user')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name','email', 'password', 'phone_number', 'email_reminder', 'text_reminder')


