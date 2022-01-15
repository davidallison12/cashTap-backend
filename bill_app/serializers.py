from os import write
from .models import User, Bill, Profile
from rest_framework import serializers 
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password


class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = ('id', 'bill_type', 'company_name', 'bill_due_date', 'min_payment', 'user')


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = "__all__"

#         def create(self, validated_data):
#             user = super(UserSerializer, self).create(validated_data)
#             user.set_password(validated_data['password'])
#             user.save()
#             return user

class UserSerializer(serializers.ModelSerializer): #https://medium.com/django-rest/django-rest-framework-login-and-register-user-fd91cf6029d5
    # password = serializers.Charfield(write_only=True)
    password = serializers.CharField(write_only=True, validators=[validate_password])
    
    
    class Meta:
        model = User
        fields = ("username", "password", "first_name", "last_name", "email")
        # write_only_fields = ('password')

    

    def create(self, validated_data):

        user = User.objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            password=make_password(validated_data['password'])
        )
        

        user.save()
        return user
    



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"

