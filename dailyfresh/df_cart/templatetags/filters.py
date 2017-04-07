# coding=utf-8
from django.template import Library
register = Library()


@register.filter
def multi_price(value1, value2):
    return float(value1) * float(value2)
