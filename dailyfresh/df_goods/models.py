# coding=utf-8
from django.db import models
from tinymce.models import HTMLField
# Create your models here.


class TypeInfoManager(models.Manager):
    def get_queryset(self):
        return super(TypeInfoManager, self).get_queryset().filter(is_delete=False)


class GoodsInfoManager(models.Manager):
    def get_queryset(self):
        return super(GoodsInfoManager, self).get_queryset().filter(g_is_delete=False)


class TypeInfo(models.Model):
    title = models.CharField(max_length=20)
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.title.encode('utf-8')

    Types = TypeInfoManager()


class GoodsInfo(models.Model):
    g_title = models.CharField(max_length=20)
    g_pic = models.ImageField(upload_to='goods')
    g_price = models.DecimalField(max_digits=5, decimal_places=2)
    g_unit = models.CharField(max_length=20, default='500g')
    g_click = models.IntegerField()
    g_profiles = models.CharField(max_length=200)
    g_stock = models.IntegerField()
    g_content = HTMLField()
    g_is_delete = models.BooleanField(default=False)
    g_type = models.ForeignKey(TypeInfo)

    Goods = GoodsInfoManager()

    def __str__(self):
        return self.g_title.encode('utf-8')
