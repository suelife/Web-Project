from django.shortcuts import render,HttpResponse
from sport.models import SportItem, SportRecord
from sport.serializers import SportItemSerializer,SportRecordSerializer
from rest_framework import viewsets
from . import modelField
import datetime
from django.db.models import Count,Sum
import requests
import json

# =============   sport ViewSet  ===============================
# function desc. : 運動項目列表 ViewSet/
# parameter : 
# create user : Luffy Lin
# modify user : Luffy Lin
# modify date : 2018/09/21
class SportItemViewSet(viewsets.ModelViewSet):
    queryset = SportItem.objects.all()
    serializer_class = SportItemSerializer

# function desc. : 個人運動紀錄管理 ViewSet
# parameter : 
# create user : Luffy Lin
# modify user : Luffy Lin
# modify date : 2018/09/21
class SportRecordViewSet(viewsets.ModelViewSet):
    queryset = SportRecord.objects.all()
    serializer_class = SportRecordSerializer

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
        return 1

# =============   sport page deal  ===============================
# function desc. : 運動項目列表
# parameter : 
# create user : Luffy Lin
# modify user : Luffy Lin
# modify date : 2018/09/21
def item(request):
    if chklogin(request):
        path = request.path
        return HttpResponse("<script>alert('請先登入');location.href = '/limit/login?url={}'</script>".format(path))

    title = "運動項目列表"
    sports = SportItem.objects.filter(state='1')
    fields = modelField.getField('sport','SportItem')[0:4]
    return render(request, 'sport/sportItem.html', locals())

# function desc. : 取得政府資料交易平台運動項目消耗熱量表，並更新或新增
# parameter : 
# create user : Luffy Lin
# modify user : Luffy Lin
# modify date : 2018/10/3
def itemScraping(request):
    if('userid' in request.session):
        userid = request.session["userid"]
    
    else:
        userid = '1'; username='Luffy'
    url = "https://quality.data.gov.tw/dq_download_json.php?nid=8494&md5_url=db669862c24a114b45629f6a27fd3881"
    
    try:
        r = requests.post(url)
        r.encoding = 'utf-8'
        items = r.json()
            
        for item in items:
            name =item["運動項目"]
            cal = item["消耗熱量(大卡/公斤體重/小時)"]
            sport = SportItem.objects.filter(name = name)
            if(sport):
                sport[0].cal = cal
                sport[0].save()
            else:
                SportItem.objects.create(name=name, cal=cal, state=1, cuser_id=userid)
    
    except err:
        return HttpResponse(err, content_type="text/plain")
    
    return HttpResponse(1, content_type="text/plain")

# function desc. : 個人運動紀錄管理
# parameter : id(預設:0)
# create user : Luffy Lin
# modify user : Luffy Lin
# modify date : 2018/09/21
def record(request,id = 0):
    if chklogin(request):
        path = request.path
        return HttpResponse("<script>alert('請先登入');location.href = '/limit/login?url={}'</script>".format(path))

    if('userid' in request.session):
        userid = request.session["userid"]
    #測試暫時使用
    else:
        userid = '1'; username='Luffy'

    title = "個人運動紀錄管理"
    # fields = modelField.getField('sport','SportRecord')[0:8]
    
    sports = SportItem.objects.filter(state='1')
    datas = SportRecord.objects.filter(cuser=userid).order_by('-sdate')
    
    return render(request, 'sport/sportRecord.html', locals())

# # function desc. : 個人運動紀錄 - 圖表
# # parameter : id
# # create user : Luffy Lin
# # modify user : Luffy Lin
# # modify date : 2018/09/27   
def chartData(request,s_date,e_date):
    if chklogin(request):
        path = request.path
        return HttpResponse("<script>alert('請先登入');location.href = '/limit/login?url={}'</script>".format(path))

    if('userid' in request.session):
        userid = request.session["userid"]
    #測試暫時使用
    else:
        userid = '1'; username='Luffy'
    datas = SportRecord.objects.filter(cuser=userid, sdate__range=(s_date, e_date)).values('sportid').annotate(dcount=Count('sportid'),dsum=Sum('duration')).values('sportid__name','dcount','dsum')
    datas = json.dumps(list(datas))
  

    return HttpResponse(datas, content_type="application/json")

# # function desc. : 個人運動紀錄 - 圖表
# # parameter : id
# # create user : Luffy Lin
# # modify user : Luffy Lin
# # modify date : 2018/09/27   
def chartPie(request):
    if chklogin(request):
        path = request.path
        return HttpResponse("<script>alert('請先登入');location.href = '/limit/login?url={}'</script>".format(path))
    return render(request, 'sport/sportChartPie.html')