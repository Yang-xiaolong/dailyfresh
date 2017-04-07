# coding=utf-8
from df_user.models import *


def get_count(request):
    try:
        user = UserInfo.objects.get(id=request.session['user_id'])
        count = user.cartinfo_set.count()
    except:
        count = 0
    return count
