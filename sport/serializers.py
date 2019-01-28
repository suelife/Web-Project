from rest_framework import serializers
from sport.models import SportItem, SportRecord

class SportItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SportItem
        fields ='__all__'

class SportRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = SportRecord
        fields ='__all__'