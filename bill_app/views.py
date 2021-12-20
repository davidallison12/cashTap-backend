from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, generics, permissions
from .serializers import BillSerializer, ProfileSerializer, UserSerializer
from .models import Bill, User, Profile
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.


def home(request):
    return HttpResponse('<h1>This is the Home Page</h1>')


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class BillView(viewsets.ModelViewSet): 
    serializer_class = BillSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):  #https://stackoverflow.com/questions/34968725/djangorestframework-how-to-get-user-in-viewset
        user = self.request.user
        print(user)
        return Bill.objects.filter(user=user)

    # user = request.user



class UserCreateView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer


class ProfileView(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    
    def get_queryset(self):  #https://stackoverflow.com/questions/34968725/djangorestframework-how-to-get-user-in-viewset
        user = self.request.user
        print(user)
        return Profile.objects.filter(user=user)
