from django.db import models


#角色
class Role(models.Model):
    role    = models.CharField(max_length=20, blank=True, unique= True)         #角色名稱
    desc    = models.CharField(max_length=500, blank=True, null=True)           #角色描述
    state   = models.BooleanField()                                             #狀態(1:啟用,0:停用)
    cdate   = models.DateTimeField(auto_now_add=True)                           #建立日期
    mdate   = models.DateTimeField(auto_now=True)                               #修改日期
    class Meta:
        db_table = 'limit_role'      

#功能選單
class Menu(models.Model):
    name    = models.CharField(max_length=20, blank=True)                       #名稱
    level   = models.IntegerField()                                             #階層
    parent  = models.ForeignKey('self',models.DO_NOTHING)                       #父節點
    index   = models.IntegerField()                                             #排序
    state   = models.BooleanField()                                             #狀態(1:啟用,0:停用)
    cdate   = models.DateTimeField(auto_now_add=True)                           #建立日期
    mdate   = models.DateTimeField(auto_now=True)                               #修改日期
    class Meta:
        db_table = 'limit_menu'

#角色功能權限
class RoleMenu(models.Model):
    menuid  = models.ForeignKey(Menu,models.DO_NOTHING)                         #功能
    roleid  = models.ForeignKey(Role,models.DO_NOTHING)                         #階層
    index   = models.IntegerField()                                             #排序
    state   = models.BooleanField()                                             #狀態(1:啟用,0:停用)
    cdate   = models.DateTimeField(auto_now_add=True)                           #建立日期
    mdate   = models.DateTimeField(auto_now=True)                               #修改日期
    class Meta:
        db_table = 'limit_rolemenu'

#使用者資料表
class User(models.Model):
    email   = models.CharField(max_length=200,unique=True)                      #email
    name    = models.CharField(max_length=50)                                   #使用者名稱
    birthday= models.DateField()                                                #生日
    gender  = models.CharField(max_length=6)                                    #性別
    password= models.CharField(max_length=20)                                   #密碼
    cdate   = models.DateTimeField(auto_now_add=True)                           #建立日期
    mdate   = models.DateTimeField(auto_now=True)                               #修改日期
    class Meta:
        db_table = 'limit_user'

#使用者角色資料表
class UserRole(models.Model):
    userid = models.ForeignKey(User,models.DO_NOTHING)                          #userid   
    roleid = models.ForeignKey(Role,models.DO_NOTHING)                          #roleid
    cdate   = models.DateTimeField(auto_now_add=True)                           #建立日期
    mdate   = models.DateTimeField(auto_now=True)                               #修改日期
    class Meta:
        db_table = 'limit_userrole'