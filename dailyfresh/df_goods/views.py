# coding=utf-8
from models import *
from django.shortcuts import render
from django.core.paginator import Paginator
from collections import deque
from utils import get_cart_goods_count

# Create your views here.


def index(request):
    type_data = TypeInfo.Types.all()
    fruit_data = GoodsInfo.Goods.filter(g_type__title='新鲜水果').order_by('-id')
    fruit_click = GoodsInfo.Goods.filter(g_type__title='新鲜水果').order_by('-g_click')
    type_data1, type_data2, type_data3, type_data4, type_data5, type_data6 = type_data

    seafood_data = GoodsInfo.Goods.filter(g_type__title='海鲜水产').order_by('-id')
    seafood_click = GoodsInfo.Goods.filter(g_type__title='海鲜水产').order_by('-g_click')

    meat_data = GoodsInfo.Goods.filter(g_type__title='猪牛羊肉').order_by('-id')
    meat_click = GoodsInfo.Goods.filter(g_type__title='猪牛羊肉').order_by('-g_click')

    egg_data = GoodsInfo.Goods.filter(g_type__title='禽类蛋品').order_by('-id')
    egg_click = GoodsInfo.Goods.filter(g_type__title='禽类蛋品').order_by('-g_click')

    vegetables_data = GoodsInfo.Goods.filter(g_type__title='新鲜蔬菜').order_by('-id')
    vegetables_click = GoodsInfo.Goods.filter(g_type__title='新鲜蔬菜').order_by('-g_click')

    ice_data = GoodsInfo.Goods.filter(g_type__title='速冻食品').order_by('-id')
    ice_click = GoodsInfo.Goods.filter(g_type__title='速冻食品').order_by('-g_click')
    count = get_cart_goods_count.get_count(request)
    context = {
        'type': 'index',
        'title': '天天生鲜-首页',
        'type_data1': type_data1,
        'type_data2': type_data2,
        'type_data3': type_data3,
        'type_data4': type_data4,
        'type_data5': type_data5,
        'type_data6': type_data6,
        'count': count,
        'fruit': {
            'click': fruit_click[0:3],
            'content': fruit_data[0:4]
        },
        'seafood': {
            'click': seafood_click[0:2],
            'content': seafood_data[0:4]
        },
        'meat': {
            'click': meat_click[0:3],
            'content': meat_data[0:4]
        },
        'egg': {
            'click': egg_click[0:3],
            'content': egg_data[0:4]
        },
        'vegetables': {
            'click': vegetables_click[0:3],
            'content': vegetables_data[0:4]
        },
        'ice': {
            'click': ice_click[0:3],
            'content': ice_data[0:4]
        }
    }
    return render(request, 'df_goods/index.html', context)


def goods_list(request):
    type_data = TypeInfo.Types.all()
    type_data1, type_data2, type_data3, type_data4, type_data5, type_data6 = type_data
    g_type = request.GET.get('g_type')
    p_index = request.GET.get('p_index')
    sort = request.GET.get('sort')
    click_data = '0'
    if sort == 'default':
        click_data = GoodsInfo.Goods.filter(g_type__title=g_type).order_by('-id')
    elif sort == 'price':
        click_data = GoodsInfo.Goods.filter(g_type__title=g_type).order_by('-g_price')
    elif sort == 'click':
        click_data = GoodsInfo.Goods.filter(g_type__title=g_type).order_by('-g_click')

    count = get_cart_goods_count.get_count(request)
    new_data = GoodsInfo.Goods.filter(g_type__title=g_type).order_by('-id')[0:2]
    page = Paginator(click_data, 10)
    p_index = int(p_index)
    list1 = page.page(p_index)
    p_list = page.page_range
    context = {
        'count': count,
        'type': 'list',
        'title': '天天生鲜-商品列表',
        'g_type': g_type,
        'new': new_data,
        'list': list1,
        'p_list': p_list,
        'p_index': p_index,
        'sort': sort,
        'type_data1': type_data1,
        'type_data2': type_data2,
        'type_data3': type_data3,
        'type_data4': type_data4,
        'type_data5': type_data5,
        'type_data6': type_data6
    }
    return render(request, 'df_goods/list.html', context)


def goods_detail(request):
    type_data = TypeInfo.Types.all()
    type_data1, type_data2, type_data3, type_data4, type_data5, type_data6 = type_data
    g_type = request.GET.get('g_type')
    g_id = request.GET.get('g_id')
    new_data = GoodsInfo.Goods.filter(g_type__title=g_type).order_by('-id')[0:2]
    detail_data = GoodsInfo.Goods.get(id=g_id)
    detail_data.g_click += 1
    detail_data.save()
    count = get_cart_goods_count.get_count(request)
    context = {
        'count': count,
        'type': 'detail',
        'title': '天天生鲜-商品详情',
        'g_type': g_type,
        'goods_info': detail_data,
        'new': new_data,
        'type_data1': type_data1,
        'type_data2': type_data2,
        'type_data3': type_data3,
        'type_data4': type_data4,
        'type_data5': type_data5,
        'type_data6': type_data6
    }
    response = render(request, 'df_goods/detail.html', context)
    id_list = request.COOKIES.get('goods_ids', deque([]))
    str_ = type('str')
    id_list_type = type(id_list)
    if id_list_type == str_:
        id_list = eval(id_list)
    if g_id in id_list:
        id_list.remove(g_id)
    if len(id_list) >= 5:
        id_list.pop()

    id_list.appendleft(g_id)
    response.set_cookie('goods_ids', id_list)
    return response

