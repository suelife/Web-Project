# from django.db import models

# # Create your models here.

# class On_Account(models.Model):

#     # 收支類型  存入(income(收入), outlay(支出))
#     IOtype = models.CharField(max_length = 50) 

#     # 金額 存入(幣值NT, 負號=out, 沒負號=in)         
#     money = models.IntegerField()       

#     # 消費類型 存入(food(食物), traffic(交通), recreation(娛樂), other(其他))                   
#     spendtype = models.CharField(max_length = 50, null = True)  

#     # 日期 存入(2018/09/19/15:48(24hr制))
#     date = models.DateTimeField(auto_now_add=True)  

#     # 備註 
#     remark = models.CharField(max_length = 500, null = True)

#     # 消費方式 存入(cash(現金), credit_card(信用卡))               
#     # spendmode = models.CharField(max_length = 50, null = True)
    
#     # 使用者ID FK         
#     # userid = models.IntegerField(user, models.DO_NOTHING, db_column = "id")    

#     class Meta:
#         managed = True  # <- 刪掉或改成True
#         db_table = 'on_account_local'
