from django.db import models

# class Memo(models.Model):
#     # cuser = models.ForeignKey(user,models.DO_NOTHING,db_column='id')
#     memoID = models.AutoField(primary_key=True)
#     memoTitle = models.CharField(max_length=60)
#     memoContent = models.CharField(max_length=300,null=True,blank=True)
#     memoState = models.CharField(max_length=1)
#     expiredate = models.DateField(null=True)
#     createTime = models.DateTimeField(auto_now_add=True)
#     lastUpgradeT = models.DateTimeField(auto_now=True)

#     class Meta:
#         db_table = 'Memos'