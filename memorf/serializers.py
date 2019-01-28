from rest_framework import serializers
from memorf.models import Memorf

class MemorfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Memorf
        fields = '__all__'