from django.urls import path
from . import views

app_name = 'sport'

urlpatterns = [

    path('',views.item, name = 'sportitem'),
    path('sportrecord/', views.record, name = 'sportrecord'),
    path('itemscraping/', views.itemScraping, name = 'itemscraping'),
    path('chartpie/', views.chartPie, name = 'chartpie'),
    path('chartdata/<str:s_date>/<str:e_date>/', views.chartData, name = 'chartdata'),
]
