from django import template

register = template.Library()


@register.inclusion_tag('chat/tags/header.html')
def header():
    pass
