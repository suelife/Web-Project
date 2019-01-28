from django.db import models
from limit.models import User

# Create your models here.

class On_Account(models.Model):

    # 使用者ID FK
    # 要再修改         
    userid = models.ForeignKey(User, models.DO_NOTHING, null = True, db_column = 'userid')

    # 收支類型
    IOtype = models.CharField(max_length = 50) 

    # 金額         
    money = models.IntegerField()       

    # 消費類型                   
    spendtype = models.CharField(max_length = 50, null = True)  

    # 日期
    date = models.DateTimeField(auto_now_add=True)  

    # 備註 
    remark = models.CharField(max_length = 500, null = True)

    class Meta:
        db_table = 'on_account'
