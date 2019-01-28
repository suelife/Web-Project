from django.shortcuts import render
from rest_framework import viewsets,generics
from .serializers import FoodCategoryApiSerializer,FoodListApiSerializer,DietaryRecordApiSerializer
from .models import FoodCategoryApi,FoodListApi,DietaryRecordApi
# Create your views here.

class FoodCategoryApiViewSet(viewsets.ModelViewSet):
    queryset = FoodCategoryApi.objects.all()
    serializer_class = FoodCategoryApiSerializer

class FoodListApiViewSet(viewsets.ModelViewSet):
    queryset = FoodListApi.objects.all()
    serializer_class = FoodListApiSerializer

# #回傳全部
# class DietaryRecordApiViewSet(viewsets.ModelViewSet):
#     queryset = DietaryRecordApi.objects.all()
#     serializer_class = DietaryRecordApiSerializer

#指定條件讀取資料用generics定義function
class DietaryRecordApiViewSet(generics.ListAPIView):
    serializer_class = DietaryRecordApiSerializer
    def get_queryset(self):
        
        userid = self.kwargs["userid"]
        sdate = self.kwargs["sdate"]
        edate = self.kwargs["edate"]
        queryset = DietaryRecordApi.objects.filter(userid=userid, dietarydate__range=(sdate,edate))
        return queryset
    