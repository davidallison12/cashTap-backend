from .models import User, Bill, Profile
from rest_framework import serializers 


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

class UserSerializer(serializers.ModelSerializer):
    # password = serializers.Charfield(write_only=True)
    class Meta:
        model = User
        fields = ("id", "username", "password", "first_name", "last_name", "email")
        # write_only_fields = ('password')


    def create(self, validated_data):

        user = User.objects.create_user(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email']
        )
        
        user.set_password(validated_data['password'])
        user.save()
        return user
    



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"

