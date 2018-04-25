from django import template

register = template.Library()


@register.filter
def concat_string(value_1, value_2):
    return str(value_1) + str(value_2)