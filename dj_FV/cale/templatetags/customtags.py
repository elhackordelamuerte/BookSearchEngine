from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name="transform")
@stringfilter
def first_char(value):
    return value [0]