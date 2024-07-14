from django.shortcuts import render
from rest_framework import generics
from .models import ClassPeriod
from .serializers import ClassPeriodSerializer

class ClassPeriodList(generics.ListAPIView):
    queryset = ClassPeriod.objects.all()
    serializer_class = ClassPeriodSerializer

# Create your views here.
