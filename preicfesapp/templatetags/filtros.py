from django import template

register = template.Library()

@register.filter(name='sumanumero')
def sumanumero(value, arg):
    return value + arg

@register.filter(name='ispair')
def ispair(value):
    return value % 2 == 0
