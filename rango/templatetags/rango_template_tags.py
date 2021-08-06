from django import template
from rango.models import Category

register = template.Library()

@register.inclusion_tag('wardrobe/categories.html')
def get_category_list():
    return {'categories': Category.objects.all()}