from django.shortcuts import render
from memorf.models import Memorf
from memorf.serializers import MemorfSerializer
from rest_framework import viewsets

class MemorfViewSet(viewsets.ModelViewSet):
    queryset = Memorf.objects.all()
    serializer_class = MemorfSerializer
