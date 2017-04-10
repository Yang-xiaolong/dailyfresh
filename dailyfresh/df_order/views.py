# coding=utf-8
from datetime import datetime
from django.http import JsonResponse
from django.shortcuts import render, redirect
from models import *
from df_user.models import *
from df_cart.models import *
from django.db import transaction
from df_goods.models import *
from utils import login_verification
from django.views.decorators.csrf import csrf_exempt
from decimal import Decimal

# Create your views here.


@login_verification.login
def order(request):
    """订单页面显示

    :param request: 浏览器请求
    :return:
    """

    user_id = request.session.get('user_id')
    user_info = UserInfo.objects.filter(id=user_id)
    cart_id_list = request.GET.getlist('cart_id')
    cart_info_list = []
    for cart_id in cart_id_list:
        cart_info = CartInfo.objects.get(id=cart_id)
        cart_info_list.append(cart_info)
    context = {
        'page': '提交订单',
        'user_info': user_info[0],
        'cart_info': cart_info_list
    }
    return render(request, 'df_order/place_order.html', context)


@csrf_exempt
@transaction.atomic()
@login_verification.login
def order_submit(request):
    """提交订单，进行处理
    :param request:
    :return:
    """
    tran_id = transaction.savepoint()
    o_address = request.POST.get('address')
    o_subtotal = request.POST.get('subtotals')
    user_id = request.session.get('user_id')
    goods_list = request.POST.get('goods_list')
    goods_list = goods_list.split(",")
    now = datetime.now()
    now_time = now.strftime('%Y%m%d%H%M%S')
    o_id = "%s%s" % (now_time, user_id)
    print(tran_id, o_address, o_subtotal, user_id, now_time, o_id, goods_list)
    try:
        order_info = OrderInfo()
        order_info.o_date = now
        order_info.o_id = o_id
        order_info.o_user_id = user_id
        order_info.o_subtotal = Decimal(o_subtotal)
        order_info.o_address = o_address  # 添加订单
        order_info.save()
        context = {}
        for item in goods_list:
            print(item)
            cart_info = CartInfo.objects.get(id=item)
            goods_info = GoodsInfo.Goods.get(id=cart_info.goods_id)
            if cart_info.count > goods_info.g_stock:
                context = {'state': 0}
                transaction.savepoint_rollback(tran_id)
            else:
                order_detail_info = OderDetailInfo()
                order_detail_info.goods_id = goods_info.id
                order_detail_info.order_id = o_id
                order_detail_info.price = goods_info.g_price
                order_detail_info.count = cart_info.count
                order_detail_info.save()             # 添加订单的详情信息
                cart_info.delete()
                context = {'state': 1}
        transaction.savepoint_commit(tran_id)
    except Exception :
        context = {'state': 2}
        transaction.savepoint_rollback(tran_id)
    return JsonResponse(context)


@login_verification.login
def order_pay(request):
    order_id = request.GET.get('order_id')
    order_info = OrderInfo.objects.get(o_id=order_id)
    order_info.o_is_pay = True
    order_info.save()
    return redirect('/user/user_center_order/')

