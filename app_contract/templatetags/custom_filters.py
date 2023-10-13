import calendar

from _decimal import Decimal
from django import template

register = template.Library()


@register.filter(name='to_js_decimal')
def to_js_decimal(value):
    if isinstance(value, list):
        return [float(v) for v in value]
    elif isinstance(value, str):
        return float(value)
    elif isinstance(value, Decimal):
        return float(value)
    return value


@register.filter
def calculate_percentage(value, total):
    try:
        return (value / total) * 100
    except ZeroDivisionError:
        return 0


@register.filter(name='month_name')
def month_name(month_number):
    return calendar.month_name[month_number]
