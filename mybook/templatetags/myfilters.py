# 自定义过滤器 过滤器就是python的相关函数

from django import template

# 创建一个Library类的对象
register = template.Library()

# 自定义过滤器，至少要有一个参数，最多两个参数

@register.filter(name="mod")
def mod(num):
    '''判断num是否为偶数'''
    return num % 2 == 0
@register.filter(name="mod_val")
def mod_val(num,val):
    '''判断nume是否能被val整除'''
    return num%val == 0

