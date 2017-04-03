# coding=utf-8
from models import *
from django.shortcuts import render

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
    context = {
        'title': '天天生鲜-首页',
        'type_data1': type_data1,
        'type_data2': type_data2,
        'type_data3': type_data3,
        'type_data4': type_data4,
        'type_data5': type_data5,
        'type_data6': type_data6,
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
    context = {
        'title': '天天生鲜-商品列表'
    }
    return render(request, 'df_goods/list.html', context)
