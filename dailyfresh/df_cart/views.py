# coding=utf-8
from django.shortcuts import render
from models import *
from utils import login_verification, get_cart_goods_count
from django.http import JsonResponse
# Create your views here.


@login_verification.login
def cart(request):
    user_id = request.session['user_id']
    cart_info = CartInfo.objects.filter(user_id=user_id)
    count = len(cart_info)
    context = {
        'cart_info': cart_info,
        'title': '天天生鲜-购物车',
        'page': '购物车',
        'count': count,
    }
    return render(request, 'df_cart/cart.html', context)


@login_verification.login
def add_goods(request):
    g_id = request.GET.get('g_id')
    g_count = request.GET.get('count')
    g_id = int(g_id)
    g_count = int(g_count)
    user_id = request.session['user_id']
    is_exist = CartInfo.objects.filter(goods_id=g_id, user_id=user_id)
    print('goods%s' % is_exist)
    if len(is_exist) > 0:
        is_exist[0].count += g_count
        print(is_exist[0].count)
        is_exist[0].save()
        print(g_count)
    else:
        cart = CartInfo()
        cart.user_id = user_id
        cart.goods_id = g_id
        cart.count = g_count
        cart.save()
    count = get_cart_goods_count.get_count(request)
    return JsonResponse({'count': count})


def change(request):
    cart_id = request.GET.get('cart_id')
    count = request.GET.get('count')
    count = int(count)
    context = {}
    try:
        cart = CartInfo.objects.get(id=cart_id)
        cart.count = count
        cart.save()
        context = {"count": count}
    except:
        context = {'count': 1, 'is_error': 'ok'}
    finally:
        return JsonResponse(context)


def cart_del(request):
    cart_id = request.GET.get('cart_id')
    CartInfo.objects.get(id=cart_id).delete()
    return JsonResponse({'is_delete': 'ok'})
