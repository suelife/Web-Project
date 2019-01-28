from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User,UserRole
from rest_framework import viewsets
from .serializers import UserSerializer,UserRoleSerializer
import datetime


# =============   User ViewSet  ===============================
# function desc. : 使用者 ViewSet
# parameter : 
# create user : Luffy Lin
# modify user : Luffy Lin
# modify date : 2018/10/07
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# function desc. : 使用者角色 ViewSet
# parameter : 
# create user : Luffy Lin
# modify user : Luffy Lin
# modify date : 2018/10/07
class UserRoleViewSet(viewsets.ModelViewSet):
    queryset = UserRole.objects.all()
    serializer_class = UserRoleSerializer

# function desc. : 確認是否已經登入
# parameter : 
# create user : Luffy Lin
# modify user : Luffy Lin
# modify date : 2018/10/07
def chklogin(request):
    if('userid' in request.session):
        global userid
        global username
        userid = request.session["userid"]
        username = request.COOKIES["name"]
        return 0
    else:
        #userid = '1'; username='Luffy'
        return 1

# function desc. : 使用者註冊
# parameter : 
# create user : Luffy Lin
# modify user : Luffy Lin
# modify date : 2018/10/07
def register(request): 
     if request.method =="POST":
        email = request.POST["email"]
        name = request.POST["name"]
        birthday = request.POST["birthday"]
        gender = request.POST["gender"]
        password = request.POST["password"]
        
        User.objects.create(email=email,name=name,birthday=birthday,gender=gender,password=password)
        return HttpResponse("<script>alert('註冊成功，請進行首次登入');location.href = '/limit/login/'</script>")

     return render(request,'limit/register.html',locals())

# function desc. : 使用者註冊時確認信箱是否已被註冊
# parameter : 
# create user : Luffy Lin
# modify user : Luffy Lin
# modify date : 2018/10/07
def checkEmail(request,email):
    users = User.objects.filter(email = email)
    msg = 0
    
    if users:
       msg = 1

    return HttpResponse(msg)
# function desc. : 使用者編輯
# parameter : 
# create user : Luffy Lin
# modify user : Luffy Lin
# modify date : 2018/10/07
def user(request): 
    if chklogin(request):
        path = request.path
        return HttpResponse("<script>alert('請先登入');location.href = '/limit/login?url={}'</script>".format(path))

    if request.method =="POST":
        user = User.objects.get(id = userid)
        user.email = request.POST["email"]
        user.name = request.POST["name"]
        user.birthday = request.POST["birthday"]
        user.gender = request.POST["gender"]
        user.password = request.POST["password"]
        
        response = HttpResponse("<script>alert('修改成功');location.href = '/limit/user/'</script>")
        response.set_cookie("name",user.name)#,expires=expires)
        user.save()
        return response
    
    userinfo = User.objects.get(id = userid)
    return render(request,'limit/user.html',locals())

# function desc. : 使用者登入
# parameter : 
# create user : Luffy Lin
# modify user : Luffy Lin
# modify date : 2018/10/07
def login(request):
    if("url" in request.GET):
        path = request.GET["url"]
    else:
        path = "/"
    
    if request.method =="POST":
        email = request.POST["email"]
        password = request.POST["password"]
        
        if(request.POST["captcha"] == request.session["captcha"]):
            remember = "0"
            users = User.objects.filter(email = email, password = password).values("name","id")
            if users :
                name = users[0]["name"]
                request.session["userid"] = users[0]["id"]
                response = HttpResponse("""<script>
                alert('{0}歡迎回來');
                location.href = '{1}';</script>""".format(name,path))
               
                if "remember" in request.POST.keys() :
                    enddate = datetime.datetime.now() + datetime.timedelta(days=7)
                    response.set_cookie("name",name,expires=enddate)
                else:
                    response.set_cookie("name",name)  
                
                print(users,remember)
                return response
            else:
                path ="/"
                return HttpResponse("<script>alert('登入失敗，請重新登入');location.href = '/limit/login/'</script>")
        else:
            return HttpResponse("<script>alert('驗證失敗，請重新登入');location.href = '/limit/login/'</script>")
    return render(request,'limit/login.html',locals())


# function desc. : 使用者登出
# parameter : 
# create user : Luffy Lin
# modify user : Luffy Lin
# modify date : 2018/10/07
def logout(request):
    del request.session["userid"]
    response = HttpResponse("<script>alert('登出成功');location.href = '/'</script>")
    response.delete_cookie('name')
    return response

   
# function desc. : 使用者登入時顯示數字驗證碼
# parameter : 
# create user : Luffy Lin
# modify user : Luffy Lin
# modify date : 2018/10/07
def captcha(request):    
    from django.contrib.staticfiles import finders
    import random
    # 安裝 pillow  pip install pillow
    from PIL import Image,ImageDraw,ImageFont   
    list1 = random.sample(['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'],5)
    txt = ''.join(list1)    
    
    # todo 將產生的數字及字母存到session中
    request.session['captcha'] = txt  
    
    width = 15 * 4
    height = 30
    image = Image.new('RGB', (width, height), (255, 255, 255))    
    # 下載字體https://fonts.google.com/
    thefont = finders.find('../static/fonts/Kavivanar-Regular.ttf')
    font = ImageFont.truetype(thefont, 16)   
    draw = ImageDraw.Draw(image)
    draw.text((5, 5), txt,font=font, fill=(255, 0, 0))
    response = HttpResponse(content_type="image/png")
    image.save(response, "PNG")
    return response