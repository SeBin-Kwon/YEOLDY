from django import template

register = template.Library()


@register.filter()
def ranges(count=5):
    return range(1, count)
