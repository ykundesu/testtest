from django.db import models
a=(("対応済み","ok"),(("非対応","no")))
# Create your models here.
class lists(models.Model):
 Name=models.CharField("名前",max_length=50)
 money=models.FloatField("金額")
 def __str__(self):
     return self.Name
class getlist(models.Model):
 getid=models.IntegerField("上の数字を入力してください。")
 get=models.CharField("アイテム数(例)1LC1st1個)",max_length=50)
 discord=models.CharField("discord(例)ヨッピ太郎#1234)",max_length=50)
 mcid=models.CharField("mcid(例)Yoppychan)",max_length=50)
 def __str__(self):
     return self.mcid
 
