from django import template

register = template.Library()

@register.filter(name='sumapag')
def sumapag(value, arg):
    return value + (arg - 1) * 10

@register.filter(name='ispair')
def ispair(value):
    return value % 2 == 0
