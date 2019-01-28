from rest_framework import serializers
from .models import FoodCategoryApi,FoodListApi,DietaryRecordApi


class FoodCategoryApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodCategoryApi
        fields = '__all__'

class FoodListApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodListApi
        fields = '__all__'

class DietaryRecordApiSerializer(serializers.ModelSerializer):
    foodname = serializers.ReadOnlyField(source = 'foodid.foodname')
    foodcategory = serializers.ReadOnlyField(source = 'foodid.foodcategoryid.foodcategory')
    foodcalories = serializers.ReadOnlyField(source = 'foodid.foodcalories')
    foodcategoryid = serializers.ReadOnlyField(source = 'foodid.foodcategoryid.foodcategoryid')
    class Meta:
        model = DietaryRecordApi
        fields = '__all__'