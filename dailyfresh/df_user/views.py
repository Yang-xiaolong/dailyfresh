# coding=utf-8
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
from models import UserInfo
from pwd_encrypt import PwdEncrypt
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


# 注册页面
def register(request):
    context = {'title': '天天生鲜-注册'}
    return render(request, 'df_user/register.html', context)


# 注册
def register_handle(request):
    # 获取用户信息
    user_name = request.POST.get('user_name')
    u_pwd = request.POST.get('pwd')
    u_cpwd = request.POST.get('cpwd')
    u_email = request.POST.get('email')
    # 如果两次密码输入不正确, 则返回到注册页面
    if u_pwd != u_cpwd:
        return redirect('/register/')

    user_info = UserInfo()
    user_info.uName = user_name
    # 密码sha1加密
    u_pwd_sha1 = PwdEncrypt.encrypt(u_pwd)
    user_info.uPassword = u_pwd_sha1

    user_info.uEmail = u_email
    user_info.save()
    return redirect('/login/')


# 判断用户名是否存在
def user_is_exist(request):
    user_name = request.GET.get('user_name')
    try:
        UserInfo.objects.get(uName=user_name)
        is_exist = '1'
    except:
        is_exist = '0'
    finally:
        context = {'exist': is_exist}
        return JsonResponse(context)


def login(request):
    context = {'title': '天天生鲜-登录'}
    return render(request, 'df_user/login.html', context)


@csrf_exempt
def login_handle(request):
    user_name = request.POST.get('user_name')
    u_pwd = request.POST.get('pwd')
    is_remember_user_name = request.POST.get('isRememberUserName')
    user_data = UserInfo.objects.filter(uName=user_name)
    u_pwd_sha1 = PwdEncrypt.encrypt(u_pwd)
    if len(user_data) == 1:
        if u_pwd_sha1 == user_data[0].uPassword:
            response = HttpResponseRedirect('/user_center_info/')
            if is_remember_user_name == '1':
                response.set_cookie('user_name', user_name)
                request.session['user_id'] = user_data[0].id
                request.session['user_name'] = user_name
            elif is_remember_user_name != '1':
                response.set_cookie('user_name', '')
            return response
        else:
            is_login = '0'
    else:
        is_login = '1'
    context = {'login': is_login}
    return JsonResponse(context)


def user_center_info(request):
    user_info = UserInfo.objects.get(id=request.session['user_id'])
    context = {
        'title': '天天生鲜-用户中心',
        'user_name': user_info.uName,
        'user_email': user_info.uEmail,
        'user_address': user_info.uAddress
    }
    return render(request, 'df_user/user_center_info.html', context)


def user_center_order(request):
    context = {
        'title': '天天生鲜-用户中心',
    }
    return render(request, 'df_user/user_center_order.html', context)


def user_center_site(request):
    user_info = UserInfo.objects.get(id=request.session['user_id'])
    address_data = request.POST
    user_info.user_addressee = address_data.get('user_addressee')
    user_info.user_address = address_data.get('user_address')
    user_info.zip_code = address_data.get('zip_code')
    user_info.user_phone = address_data.get('user_phone')
    user_info.save()
    context = {
        'title': '天天生鲜-用户中心',
        'address_info': user_info
    }
    return render(request, 'df_user/user_center_site.html', context)

