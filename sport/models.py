from django.db import models
from limit.models import User

#運動項目
class SportItem(models.Model):
    name    = models.CharField(verbose_name ='運動項目', max_length=50, blank=True, null=True)
    cal     = models.DecimalField(verbose_name ='卡洛里(每小時/每公斤)', max_digits=5,decimal_places = 2)
    mdate   = models.DateTimeField(verbose_name ='修改日期', auto_now=True)
    
    state   = models.BooleanField(verbose_name ='狀態(1:啟用/0:停用)')
    cuser   = models.ForeignKey(User,models.DO_NOTHING, verbose_name ='建立人員')
    cdate   = models.DateTimeField(verbose_name ='建立日期', auto_now_add=True)
    class Meta:
        db_table = 'sport_sportitem'

#運動管理
class SportRecord(models.Model):
    sportid = models.ForeignKey(SportItem,models.DO_NOTHING, verbose_name ='運動項目')
    sdate   = models.DateField(verbose_name ='運動日期')
    duration = models.IntegerField(verbose_name ='運動持續時間(分鐘)')
    weight  = models.DecimalField (verbose_name ='體重', max_digits=4, decimal_places=1)
    cal     = models.DecimalField(verbose_name ='運動消耗卡洛里calorie',max_digits=7,decimal_places = 2) 
    cuser   = models.ForeignKey(User,models.DO_NOTHING, verbose_name ='建立人員',null=True)
    mdate   = models.DateTimeField(verbose_name ='修改日期', auto_now=True)
    
    cdate     = models.DateTimeField(verbose_name ='建立日期', auto_now_add=True)
    class Meta:
        db_table = 'sport_sportrecord'
    
#體重管理
class WeightRecord(models.Model):
    weight  = models.DecimalField (verbose_name ='體重(公斤)', max_digits=4, decimal_places=1)
    
    cuser   = models.ForeignKey(User,models.DO_NOTHING, verbose_name ='建立人員')
    cdate   = models.DateTimeField(verbose_name ='建立日期', auto_now_add=True)
    mdate   = models.DateTimeField(verbose_name ='修改日期', auto_now=True)
    class Meta:
        db_table = 'sport_weightrecord'