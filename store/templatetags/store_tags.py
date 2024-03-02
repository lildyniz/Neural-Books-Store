from django import template
from store.models import Category, Author
from django.utils.http import urlencode

register = template.Library()

@register.simple_tag()
def tag_categories():
    return Category.objects.all()

@register.simple_tag()
def tag_authors():
    return Author.objects.all()

@register.simple_tag()
def tag_category_all():
    return Category.objects.get(name='all')

@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)