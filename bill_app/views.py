from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import BillSerializer
from .models import Bill, User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here.
def home (request):
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
    queryset = Bill.objects.all()