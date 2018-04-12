from django import template

register = template.Library()

@register.filter
def in_question(lst, index):
    return lst.filter(to_question=index)
