from django.db import models
from limit.models import User

class Memorf(models.Model):
    cuser = models.ForeignKey(User,models.DO_NOTHING,verbose_name ='建立人員',null=True)
    memoID = models.AutoField(primary_key=True)
    memoTitle = models.CharField(max_length=40,null=True)
    memoContent = models.CharField(max_length=300,null=True,blank=True)
    memoState = models.CharField(max_length=1)
    expiredate = models.DateField(null=True)
    createTime = models.DateTimeField(auto_now_add=True)
    lastUpgradeT = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'memorf'