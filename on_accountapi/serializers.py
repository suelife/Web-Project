from rest_framework import serializers
from on_accountapi.models import On_Account

class On_AccountapiSerializer(serializers.ModelSerializer):
    class Meta:
        model = On_Account
        fields = "__all__"