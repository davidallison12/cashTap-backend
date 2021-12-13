from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import BillSerializer
from .models import Bill, User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

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

    def get_queryset(self):
        user = self.request.user
        print(user)
        return Bill.objects.filter(user=user)

    # user = request.user
