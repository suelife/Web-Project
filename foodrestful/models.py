from django.db import models
from limit.models import User

# Create your models here.
class FoodCategoryApi(models.Model):
    foodcategoryid = models.AutoField(primary_key=True)
    foodcategory = models.CharField(max_length=50)
    class Meta:
        db_table = "foodcategorysapi"

class FoodListApi(models.Model):
    foodid = models.AutoField(primary_key=True)
    foodcategoryid = models.ForeignKey(FoodCategoryApi,models.DO_NOTHING,db_column='foodcategoryid')
    foodname = models.CharField(max_length=50)
    foodcalories = models.FloatField(null=True)
    foodprotein = models.FloatField(null=True)
    foodfat = models.FloatField(null=True)
    foodfarbohydrate = models.FloatField(null=True)
    fooddescription = models.CharField(max_length=500,null=True)
    userid = models.ForeignKey(User,models.DO_NOTHING,db_column='userid',null=True)
    class Meta:
        db_table = "footlistsapi"

class DietaryRecordApi(models.Model):
    recordid = models.AutoField(primary_key=True)
    dietarydate = models.DateField()
    dietarytime = models.CharField(max_length=50)
    foodid = models.ForeignKey(FoodListApi,models.DO_NOTHING,db_column='foodid')
    share = models.FloatField(null=True)
    calories = models.FloatField(null=True)
    userid = models.ForeignKey(User,models.DO_NOTHING,db_column='userid',null=True)
    class Meta:
        db_table = "dietaryrecordsapi"
     
  