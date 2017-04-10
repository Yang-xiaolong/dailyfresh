# coding=utf-8
from django.template import Library
register = Library()


@register.filter
def minus(value):
    return value - 1


@register.filter
def minus1(value, value1):
    return value - value1


@register.filter
def add(value):
    return int(value) + 1


@register.filter
def length(value):
    return len(value)
