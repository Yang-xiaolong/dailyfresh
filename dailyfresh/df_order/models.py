from django.db import models
# Create your models here.


class OrderInfo(models.Model):
    o_id = models.CharField(max_length=20, primary_key=True)
    o_user = models.ForeignKey('df_user.UserInfo')
    o_date = models.DateField(auto_now=True)
    o_subtotal = models.DecimalField(max_digits=8, decimal_places=2)
    o_address = models.CharField(max_length=150)
    o_is_pay = models.BooleanField(default=False)


class OderDetailInfo(models.Model):
    goods = models.ForeignKey('df_goods.GoodsInfo')
    order = models.ForeignKey(OrderInfo)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    count = models.IntegerField()
