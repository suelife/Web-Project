from django.shortcuts import render
import datetime
# Create your views here.
def index(request):
    title = 'cool'
    return render(request, 'home/index.html', locals())
def real(request):
    time = datetime.datetime.now()
    return render(request, 'home/about.html', locals())
def hay(request):
    users = [{'name':'Jack', 'age':30, 'email':'jack@gmail.com'},
             {'name':'Tom', 'age':30, 'email':'tom@gmail.com'},
             {'name':'Luka', 'age':30, 'email':'luka@gmail.com'},]
    return render(request, 'home/ontact.html', locals())