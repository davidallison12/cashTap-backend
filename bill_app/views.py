from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import BillSerializer
from .models import Bill, User
# Create your views here.
def home (request):
    return HttpResponse('<h1>This is the Home Page</h1>')


class BillView(viewsets.ModelViewSet):
    serializer_class = BillSerializer
    queryset = Bill.objects.all()