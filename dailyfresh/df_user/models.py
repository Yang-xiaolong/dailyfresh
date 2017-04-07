from django.db import models
# Create your models here.


class UserInfo(models.Model):
    uName = models.CharField(max_length=20)
    uPassword = models.CharField(max_length=40)
    uEmail = models.CharField(max_length=30)
    uAddressee = models.CharField(max_length=20, default='')
    uAddress = models.CharField(max_length=100, default='')
    uZipCode = models.CharField(max_length=6, default='')
    uPhone = models.CharField(max_length=11, default='')
