from django import template
from enjoying_people.models import *

register = template.Library()

def get_categories():
    return Category.objects.all()