from django import template
register = template.Library()


@register.filter
def get_content(List, i):
    return List[int(i)].content


@register.filter
def get_created_at(List, i):
    return List[int(i)].created_at


@register.filter
def get_title(List, i):
    return List[int(i)].title
