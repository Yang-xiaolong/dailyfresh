# coding=utf-8
from django.contrib import admin
from models import *
# Register your models here.


class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_delete']


class GoodsInfoAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'g_title', 'g_pic',
        'g_price', 'g_unit', 'g_click',
        'g_profiles', 'g_stock', 'g_content', 'g_is_delete', 'g_type'
    ]
admin.site.register(TypeInfo, TypeInfoAdmin)
admin.site.register(GoodsInfo, GoodsInfoAdmin)
