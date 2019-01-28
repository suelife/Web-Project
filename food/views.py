from django.shortcuts import render,redirect
# from food.models import FoodList,FoodCategory,DietaryRecord
from foodrestful.models import FoodListApi,FoodCategoryApi,DietaryRecordApi
from limit.models import User
from django.http import HttpResponse
import json
from django.core import serializers


foodcategorys = FoodCategoryApi.objects.all()
foodlists = FoodListApi.objects.all()
dietaryrecords = DietaryRecordApi.objects.all()

#================================會員登入=============================================

# function desc. : 確認使用者是否登入
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
        return 1


# ================================index===============================================

#回傳食物應用程式首頁
def index(request):
    return render(request, 'food/index.html', locals())


# ================================list=================================================

#回傳食物清單
def list(request):
    # print(request.path)
    # 確認是否已登入會員
    # cookies中沒有name表示沒有登入過
    # 轉到登入頁面
    if chklogin(request):
        path = request.path
        return HttpResponse("<script>alert('請先登入');location.href = '/limit/login?url={}'</script>".format(path))

    # ---------------------------------------------------------------------------------
        
    foodlists = FoodListApi.objects.all()
    
    return render(request, 'food/foodlist.html', locals())


#食物清單新增ORM
def listcreate(request):
    # print(request.path)
    # 確認是否已登入會員
    # cookies中沒有name表示沒有登入過
    # 轉到登入頁面
    if chklogin(request):
        path = request.path
        return HttpResponse("<script>alert('請先登入');location.href = '/limit/login?url={}'</script>".format(path))

    # --------------------------------------------------------------------------------  

    #步驟二
    if  request.method == "POST":
        #接收表單傳過來的資料
        foodcategoryid = request.POST["foodcategoryid"]
        foodname = request.POST["foodname"]
        foodcalories = request.POST["foodcalories"]
        foodprotein = request.POST["foodprotein"]
        foodfat = request.POST["foodfat"]
        foodfarbohydrate = request.POST["foodfarbohydrate"]
        fooddescription = request.POST["fooddescription"]
        #建立人員~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        user = User.objects.get(id=userid)
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #將資料寫進資料庫
        FoodListApi.objects.create(foodcategoryid=FoodCategoryApi.objects.get(foodcategoryid=foodcategoryid),foodname=foodname,foodcalories=foodcalories,foodprotein=foodprotein,foodfat=foodfat,foodfarbohydrate=foodfarbohydrate,fooddescription=fooddescription,userid=user)
    
        return redirect('/food/list')
   
    #步驟一 GET 回傳空白的表單

    foodcategorys = FoodCategoryApi.objects.all()
    
    return render(request, 'food/listcreate.html', locals())


#食物清單刪除ORM
def listdelete(request,id):
    # print(request.path)
    # 確認是否已登入會員
    # cookies中沒有name表示沒有登入過
    # 轉到登入頁面
    if chklogin(request):
        path = request.path
        return HttpResponse("<script>alert('請先登入');location.href = '/limit/login?url={}'</script>".format(path))

    # --------------------------------------------------------------------------------  

    foodlist = FoodListApi.objects.get(foodid=id)
    foodlist.delete()

    return redirect('/food/list')


#食物清單修改ORM
def listupdate(request,id):
    # print(request.path)
    # 確認是否已登入會員
    # cookies中沒有name表示沒有登入過
    # 轉到登入頁面
    if chklogin(request):
        path = request.path
        return HttpResponse("<script>alert('請先登入');location.href = '/limit/login?url={}'</script>".format(path))

    # --------------------------------------------------------------------------------  

    #步驟二
    if  request.method == "POST":
        #接收表單傳過來的資料
        foodcategoryid = request.POST["foodcategoryid"]
        foodname = request.POST["foodname"]
        foodcalories = request.POST["foodcalories"]
        foodprotein = request.POST["foodprotein"]
        foodfat = request.POST["foodfat"]
        foodfarbohydrate = request.POST["foodfarbohydrate"]
        fooddescription = request.POST["fooddescription"]
        
        #將資料寫進資料庫
        foodlist = FoodListApi.objects.get(foodid=id)
        foodlist.foodcategoryid = FoodCategoryApi.objects.get(foodcategoryid=foodcategoryid)
        foodlist.foodname = foodname
        foodlist.foodcalories = foodcalories
        foodlist.foodprotein = foodprotein
        foodlist.foodfat = foodfat
        foodlist.foodfarbohydrate = foodfarbohydrate
        foodlist.fooddescription = fooddescription
        foodlist.save()
        return redirect('/food/list')

    #步驟一 GET 回傳空白的表單
    
    foodcategorys = FoodCategoryApi.objects.all()

    return render(request,'food/listupdate.html',locals())


# # 食物清單圖表ORM
# def listchart(request):
#     return render(request,'food/foodlistchart.html',locals())


#食物清單搜尋(ORM+ajax版) 
def listsearch(request):
    search = request.GET["search"] 
    categorys = FoodCategoryApi.objects.filter(foodcategory__contains=search)
    foodlists_name = FoodListApi.objects.filter(foodname__contains=search)
    foodlists_calories = FoodListApi.objects.filter(foodcalories__contains=search)
    json_datas = ''
    datas = []
    #判斷search是否為空值
    if search:
        if categorys:
            # datas = []
            for category in categorys:
                foodlists_category=FoodListApi.objects.filter(foodcategoryid=category.foodcategoryid)
                for foodlist in foodlists_category:
                    foodid = foodlist.foodid
                    foodname = foodlist.foodname
                    foodcategoryid = foodlist.foodcategoryid.foodcategoryid
                    foodcategory = foodlist.foodcategoryid.foodcategory
                    foodcalories =  foodlist.foodcalories
                    foodprotein = foodlist.foodprotein
                    foodfat = foodlist.foodfat
                    foodfarbohydrate = foodlist.foodfarbohydrate
                    fooddescription = foodlist.fooddescription
                    data={"foodid":foodid,"foodname":foodname,"foodcategoryid":foodcategoryid,"foodcategory":foodcategory,
                        "foodcalories":foodcalories,"foodprotein":foodprotein,"foodfat":foodfat,
                        "foodfarbohydrate":foodfarbohydrate,"fooddescription":fooddescription}
                    datas.append(data)
            # json_datas = json.dumps(datas)
            # json_datas = serializers.serialize("json",datas)
            # return HttpResponse(json_datas)
        
        if foodlists_name:
            # datas = []
            for foodlist in foodlists_name:
                foodid = foodlist.foodid
                foodname = foodlist.foodname
                foodcategoryid = foodlist.foodcategoryid.foodcategoryid
                foodcategory = foodlist.foodcategoryid.foodcategory
                foodcalories =  foodlist.foodcalories
                foodprotein = foodlist.foodprotein
                foodfat = foodlist.foodfat
                foodfarbohydrate = foodlist.foodfarbohydrate
                fooddescription = foodlist.fooddescription
                #判斷datas裡有沒有資料
                #如果datas有資料
                if datas:
                    unappended = True
                    for food in datas:
                        #如果datas裡已經有此筆資料把unappended改成False並離開迴圈
                        if food["foodid"] == foodid:
                            unappended = False
                            break
                    #如果unappended是True把資料加進去
                    if unappended:
                        data={"foodid":foodid,"foodname":foodname,"foodcategoryid":foodcategoryid,"foodcategory":foodcategory,
                            "foodcalories":foodcalories,"foodprotein":foodprotein,"foodfat":foodfat,
                            "foodfarbohydrate":foodfarbohydrate,"fooddescription":fooddescription}
                        datas.append(data)     
                #如果datas沒有資料直接加進去
                else: 
                    data={"foodid":foodid,"foodname":foodname,"foodcategoryid":foodcategoryid,"foodcategory":foodcategory,
                        "foodcalories":foodcalories,"foodprotein":foodprotein,"foodfat":foodfat,
                        "foodfarbohydrate":foodfarbohydrate,"fooddescription":fooddescription}
                    datas.append(data)
            # json_datas = json.dumps(datas)
            # json_datas = serializers.serialize("json",datas)
            # return HttpResponse(json_datas)

        if  foodlists_calories:  
            # datas = []
            for foodlist in foodlists_calories:
                foodid = foodlist.foodid
                foodname = foodlist.foodname
                foodcategoryid = foodlist.foodcategoryid.foodcategoryid
                foodcategory = foodlist.foodcategoryid.foodcategory
                foodcalories =  foodlist.foodcalories
                foodprotein = foodlist.foodprotein
                foodfat = foodlist.foodfat
                foodfarbohydrate = foodlist.foodfarbohydrate
                fooddescription = foodlist.fooddescription
                if datas:
                    unappended = True
                    for food in datas:
                        if food["foodid"] == foodid:
                            unappended = False
                            break
                    if unappended:
                        data={"foodid":foodid,"foodname":foodname,"foodcategoryid":foodcategoryid,"foodcategory":foodcategory,
                            "foodcalories":foodcalories,"foodprotein":foodprotein,"foodfat":foodfat,
                            "foodfarbohydrate":foodfarbohydrate,"fooddescription":fooddescription}
                        datas.append(data)   
                else: 
                    data={"foodid":foodid,"foodname":foodname,"foodcategoryid":foodcategoryid,"foodcategory":foodcategory,
                        "foodcalories":foodcalories,"foodprotein":foodprotein,"foodfat":foodfat,
                        "foodfarbohydrate":foodfarbohydrate,"fooddescription":fooddescription}
                    datas.append(data)
            # json_datas = json.dumps(datas)
            # json_datas = serializers.serialize("json",datas)
        json_datas = json.dumps(datas)
        return HttpResponse(json_datas)
    else:
        json_datas = json.dumps(datas)
        return HttpResponse(json_datas)
    
    
#=================================record================================================

#回傳紀錄表
def record(request):
    # print(request.path)
    # 確認是否已登入會員
    # cookies中沒有name表示沒有登入過
    # 轉到登入頁面
    if chklogin(request):
        path = request.path
        return HttpResponse("<script>alert('請先登入');location.href = '/limit/login?url={}'</script>".format(path))

    # --------------------------------------------------------------------------------

    dietaryrecords = DietaryRecordApi.objects.filter(userid=userid)
    return render(request, 'food/dietaryrecord.html', locals())


#新增紀錄ORM
def recordcreate(request):
    # print(request.path)
    # 確認是否已登入會員
    # cookies中沒有name表示沒有登入過
    # 轉到登入頁面
    if chklogin(request):
        path = request.path
        return HttpResponse("<script>alert('請先登入');location.href = '/limit/login?url={}'</script>".format(path))

    # --------------------------------------------------------------------------------  

    #步驟二
    if  request.method == "POST":
        #接收表單傳過來的資料
        dietarydate = request.POST["dietarydate"]
        dietarytime = request.POST["dietarytime"]
        foodcategoryid = request.POST["foodcategoryid"]
        foodid = request.POST["foodid"]
        share = float(request.POST["share"])
        foodlists = FoodListApi.objects.get(foodid=foodid)
        calories = foodlists.foodcalories * share
        #建立人員~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        user = User.objects.get(id=userid)
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #將資料寫進資料庫
        DietaryRecordApi.objects.create(foodid=FoodListApi.objects.get(foodid=foodid),dietarydate=dietarydate,dietarytime=dietarytime,share=share,calories=calories,userid=user)
    
        return redirect('/food/record')

    #步驟一 GET 回傳空白的表單
    
    foodlists = FoodListApi.objects.all()
    foodcategorys = FoodCategoryApi.objects.all()
    
    return render(request, 'food/recordcreate.html', locals())


#刪除紀錄ORM
def recorddelete(request,id):
    # print(request.path)
    # 確認是否已登入會員
    # cookies中沒有name表示沒有登入過
    # 轉到登入頁面
    if chklogin(request):
        path = request.path
        return HttpResponse("<script>alert('請先登入');location.href = '/limit/login?url={}'</script>".format(path))

    # --------------------------------------------------------------------------------  

    dietaryrecord = DietaryRecordApi.objects.get(recordid=id)
    dietaryrecord.delete()

    return redirect('/food/record')


#修改紀錄ORM
def recordupdate(request,id):
    # print(request.path)
    # 確認是否已登入會員
    # cookies中沒有name表示沒有登入過
    # 轉到登入頁面
    if chklogin(request):
        path = request.path
        return HttpResponse("<script>alert('請先登入');location.href = '/limit/login?url={}'</script>".format(path))

    # --------------------------------------------------------------------------------  

    #步驟二
    if  request.method == "POST":
        #接收表單傳過來的資料
        dietarydate = request.POST["dietarydate"]
        dietarytime = request.POST["dietarytime"]
        foodcategoryid = request.POST["foodcategoryid"]
        foodid = request.POST["foodid"]
        share = float(request.POST["share"])
        foodlists = FoodListApi.objects.get(foodid=foodid)
        calories = foodlists.foodcalories * share
        
        #將資料寫進資料庫
        dietaryrecord = DietaryRecordApi.objects.get(recordid=id)
        dietaryrecord.dietarydate = dietarydate
        dietaryrecord.dietarytime = dietarytime
        dietaryrecord.foodid = FoodListApi.objects.get(foodid=foodid)
        dietaryrecord.share = share
        dietaryrecord.calories = calories
        dietaryrecord.save()
        return redirect('/food/record')

    #步驟一 GET 回傳空白的表單
    
    foodlists = FoodListApi.objects.all()
    foodcategorys = FoodCategoryApi.objects.all()

    return render(request,'food/recordupdate.html',locals())


#紀錄圖表ORM
def recordchart(request):
    # print(request.path)
    # 確認是否已登入會員
    # cookies中沒有name表示沒有登入過
    # 轉到登入頁面
    if chklogin(request):
        path = request.path
        return HttpResponse("<script>alert('請先登入');location.href = '/limit/login?url={}'</script>".format(path))

    # --------------------------------------------------------------------------------  
    luserid = userid
    return render(request,'food/dietaryrecordchart.html',locals())


#回傳紀錄表(ajax版的飲食紀錄)
def record_ajax(request):
    # print(request.path)
    # 確認是否已登入會員
    # cookies中沒有name表示沒有登入過
    # 轉到登入頁面
    if chklogin(request):
        path = request.path
        return HttpResponse("<script>alert('請先登入');location.href = '/limit/login?url={}'</script>".format(path))

    # --------------------------------------------------------------------------------
    luserid = userid
    foodlists = FoodListApi.objects.all()
    foodcategorys = FoodCategoryApi.objects.all()
    return render(request,'food/dietaryrecord_ajax.html',locals())


# =================================把資料寫進資料庫======================================


def datatosql(requset):
    with open("foodlists_json.json",'r',encoding = 'utf-8') as json_data:
        python_obj = json.load(json_data)
        for foodlist in python_obj:
            FoodListApi.objects.create(foodcategoryid = FoodCategoryApi.objects.get(foodcategory = foodlist["foodcategory"]),
                                       foodname = foodlist["foodname"],
                                       foodcalories = foodlist["foodcalories"],
                                       foodprotein = foodlist["foodprotein"],
                                       foodfat = foodlist["foodfat"],
                                       foodfarbohydrate = foodlist["foodfarbohydrate"],
                                       fooddescription = foodlist["fooddescription"]
                                      )
