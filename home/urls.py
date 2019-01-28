from django.urls import path
from home import views
app_name = 'base'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('about/', views.real, name = 'about'),
    path('contant/', views.hay, name = 'contact'),
]
