from django import template
from enjoying_people.models import *

register = template.Library()


@register.simple_tag(name='getcats')
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('enjoying_people/list_categories.html')
def show_categories():
    cats = Category.objects.all()
    return {"cats": cats}