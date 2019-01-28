from django.shortcuts import render
from on_accountapi.models import On_Account
from on_accountapi.serializers import On_AccountapiSerializer
from rest_framework import viewsets

# Create your views here.

class On_AccountapiViewSet(viewsets.ModelViewSet):
    queryset = On_Account.objects.all()
    serializer_class = On_AccountapiSerializer