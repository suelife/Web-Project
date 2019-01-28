from django.shortcuts import render, redirect
from datetime import datetime
from django.http import HttpResponse
from limit.models import User

# Create your views here.
def chklogin(request):
    if('userid' in request.session):
        global userid
        global username
        userid = request.session["userid"]
        username = request.COOKIES["name"]
        return 0
    else:
        return 1

def index(request):
    # function desc. : 確認使用者是否登入
    # parameter : 
    # create user : Luffy Lin
    # modify user : Luffy Lin
    # modify date : 2018/10/07
    
    if chklogin(request):
        path = request.path
        return HttpResponse("<script>alert('請先登入');location.href = '/limit/login?url={}'</script>".format(path))
    
    return render(request, 'on_account/index.html', locals())

def chatarea(request):
    # function desc. : 確認使用者是否登入
    # parameter : 
    # create user : Luffy Lin
    # modify user : Luffy Lin
    # modify date : 2018/10/07
    
    if chklogin(request):
        path = request.path
        return HttpResponse("<script>alert('請先登入');location.href = '/limit/login?url={}'</script>".format(path))

    return render(request, 'on_account/chartarea.html', locals())

def catchid(request):
    return HttpResponse(userid)