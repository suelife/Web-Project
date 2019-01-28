from django.shortcuts import render,redirect,HttpResponse
from memorf.models import Memorf
from limit.models import User
from django.db.models import F
import datetime


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

    # asc(nulls_last=True)
    memot = Memorf.objects.filter(memoState='t',cuser=userid).order_by(F('expiredate').asc(nulls_last=True))
    memod = Memorf.objects.filter(memoState='d',cuser=userid).order_by(F('expiredate').asc(nulls_last=True))
    memof = Memorf.objects.filter(memoState='f',cuser=userid).order_by(F('expiredate').asc(nulls_last=True))
    user = User.objects.get(id=userid)
    today = datetime.date.today()
    

    if request.method == 'POST':
        memoTitle = request.POST['createTit']
        memoContent = request.POST['createCon']
        expiredate = None
        if request.POST['createED']:
            expiredate = request.POST['createED']
        print(userid)
        print(type(userid))
        Memorf.objects.create(memoTitle=memoTitle,memoContent=memoContent,expiredate=expiredate,memoState='t',cuser=user)
        return redirect('/memo')

    return render(request,'memo/index.html',locals())

def update(request,id):
    memo = Memorf.objects.get(memoID=id)
    memo.memoTitle = request.POST['memoTitle']
    memo.memoContent = request.POST['memoContent']
    memo.memoState = request.POST['memoState']

    if request.POST['expiredate']:
        memo.expiredate = request.POST['expiredate']

    memo.save()

    return redirect('/memo')

def archive(request):
    if chklogin(request):
        path = request.path
        return HttpResponse("<script>alert('請先登入');location.href = '/limit/login?url={}'</script>".format(path))
    
    memoa = Memorf.objects.filter(memoState='a',cuser=userid).order_by(F('expiredate').asc(nulls_last=True))
    return render(request,'memo/archive.html',locals())

# # function desc. : 個人運動紀錄 - 圖表
# # parameter : id
# # create user : Luffy Lin
# # modify user : Luffy Lin
# # modify date : 2018/09/27   
def chartData(request,s_date,e_date):

    userid = request.session["userid"]
    user = User.objects.get(id=userid)
    
    # count = Memorf.objects.filter(cuser=userid, expiredate__range=(s_date, e_date)).values('memoState').annotate(dcount=Count('memoState')).values('memoState','dcount')
    tasks = Memorf.objects.filter(cuser=user,expiredate__range=(s_date, e_date))

    archive = Memorf.objects.filter(cuser=user,memoState='a',expiredate__range=(s_date, e_date)).count()
    finish = Memorf.objects.filter(cuser=user,memoState='f',expiredate__range=(s_date, e_date)).count()
    todo = tasks.exclude(memoState='f').exclude(memoState='a')
   
    today = datetime.date.today()
    overdue = 0
    for task in todo:
        if task.expiredate < today:
            overdue += 1
    
    todoc = todo.count() - overdue
    count = str([todoc, finish, archive, overdue])
    # count = json.dumps(count)
    return HttpResponse(count, content_type="text/plain")

def chartPie(request):
    if chklogin(request):
        path = request.path
        return HttpResponse("<script>alert('請先登入');location.href = '/limit/login?url={}'</script>".format(path))
    return render(request, 'memo/memoChartPie.html')