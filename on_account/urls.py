from django.urls import path
from . import views

app_name = 'on_account'
urlpatterns = [
    path('', views.index, name = 'index'),

    path('chatarea/',views.chatarea,name="chatarea"),

    path('catch/',views.catchid,name="catchid"),
]