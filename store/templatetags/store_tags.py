from django import template
from store.models import Category, Author

register = template.Library()

@register.simple_tag()
def tag_categories():
    return Category.objects.all()

@register.simple_tag()
def tag_authors():
    return Author.objects.all()