from django.urls import path
from . import views

app_name = 'limit'

urlpatterns = [
    path('user/',views.user,name="user"),
    path('register/',views.register,name="register"),
    path('check/<str:email>', views.checkEmail, name='checkEmail'),
    path('login/',views.login,name="login"), 
    path('logout/',views.logout,name="logout"), 
    path('captcha/', views.captcha, name='captcha'),
    path('check/<str:email>', views.checkEmail, name='checkEmail'),
]
