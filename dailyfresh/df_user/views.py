# coding=utf-8
from collections import deque

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator

from utils import login_verification
from utils.pwd_encrypt import PwdEncrypt
from models import *
from df_goods.models import *
from df_order.models import *


# 注册页面
def register(request):
    context = {'title': '天天生鲜-注册'}
    return render(request, 'df_user/register.html', context)


# 注册功能
def register_handle(request):
    # 获取输入的信息用户信息
    user_name = request.POST.get('user_name')
    u_pwd = request.POST.get('pwd')
    u_cpwd = request.POST.get('cpwd')
    u_email = request.POST.get('email')

    # 判断两次输入的密码是否一致
    if u_pwd != u_cpwd:
        return redirect('/user/register/')

    # 将获取到的用户信息，保存到数据库里面
    user_info = UserInfo()
    user_info.uName = user_name
    u_pwd_sha1 = PwdEncrypt.encrypt(u_pwd)  # 密码sha1加密
    user_info.uPassword = u_pwd_sha1
    user_info.uEmail = u_email
    user_info.save()

    return redirect('/user/login/')


# 在注册时用来判断用户名是否已经存在
def user_is_exist(request):
    user_name = request.GET.get('user_name')
    is_exist = '0'
    try:
        UserInfo.objects.get(uName=user_name)
        is_exist = '1'
    except UserInfo.DoesNotExist:
        is_exist = '0'
    finally:
        context = {'exist': is_exist}
        return JsonResponse(context)


# 登录页面
def login(request):
    user_name = request.COOKIES.get('user_name', '')
    context = {
        'title': '天天生鲜-登录',
        'user_name': user_name
    }
    return render(request, 'df_user/login.html', context)


# 登陆时进行的账号，密码验证
@csrf_exempt
def login_handle(request):
    user_name = request.POST.get('user_name')
    u_pwd = request.POST.get('pwd')
    is_remember_user_name = request.POST.get('isRememberUserName')

    user_data = UserInfo.objects.filter(uName=user_name)
    u_pwd_sha1 = PwdEncrypt.encrypt(u_pwd)

    if len(user_data) == 1:
        if u_pwd_sha1 == user_data[0].uPassword:
            url = request.COOKIES.get('url', '/')
            is_login = url
            json = JsonResponse({'login': is_login})
            json.set_cookie('url', '', max_age=-1)
            if is_remember_user_name == '1':
                json.set_cookie('user_name', user_name)
            elif is_remember_user_name == '0':
                json.set_cookie('user_name', '')
            json.set_cookie('is_remember_user_name', is_remember_user_name)
            request.session['user_id'] = user_data[0].id
            request.session['user_name'] = user_name
            return json
        else:
            is_login = '0'
    else:
        is_login = '1'
    context = {'login': is_login}
    return JsonResponse(context)


# 个人信息
@login_verification.login
def user_center_info(request):
    user_info = UserInfo.objects.get(id=request.session['user_id'])

    goods_list = deque([])
    id_list = request.COOKIES.get('goods_ids', deque([]))
    if isinstance(id_list, str):
        id_list = eval(id_list)
    for g_id in id_list:
        goods_list.append(GoodsInfo.Goods.get(id=int(g_id)))

    context = {
        'title': '天天生鲜-用户中心',
        'user_name': request.session['user_name'],
        'user_email': user_info.uEmail,
        'user_address': user_info.uAddress,
        'page': 'info',
        'goods_list': goods_list,
    }

    return render(request, 'df_user/user_center_info.html', context)


# 订单信息
@login_verification.login
def user_center_order(request):
    user_id = request.session.get('user_id')
    order_info = OrderInfo.objects.filter(o_user_id=user_id).order_by('-o_id')
    order_detail_info_list = []
    for item in order_info:
        order_detail_info = OderDetailInfo.objects.filter(order_id=item.o_id)
        order_detail_info_list.append(order_detail_info)

    page = Paginator(order_detail_info_list, 2)
    p_index = request.GET.get('p_index', "1")
    p_index = int(p_index)
    list1 = page.page(p_index)
    p_list = page.page_range

    context = {
        'title': '天天生鲜-用户中心',
        'page': 'order',
        'order_info': order_detail_info_list,
        'p_list': p_list,
        'list1': list1,
        'p_index': p_index
    }
    return render(request, 'df_user/user_center_order.html', context)


# 地址管理
@login_verification.login
def user_center_site(request):
    user_info = UserInfo.objects.get(id=request.session['user_id'])

    if request.method == "post":
        address_data = request.POST
        user_info.uAddressee = address_data.get('user_addressee')
        user_info.uAddress = address_data.get('user_address')
        user_info.uZipCode = address_data.get('zip_code')
        user_info.uPhone = address_data.get('user_phone')
        user_info.save()

    context = {
        'title': '天天生鲜-用户中心',
        'address_info': user_info,
        'page': 'site',
    }
    return render(request, 'df_user/user_center_site.html', context)


# 退出
def logout(request):
    request.session.flush()
    return redirect('/user/login')
