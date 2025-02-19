from django import template
from myresume.models import Category
import myresume.views as views


register = template.Library()


@register.inclusion_tag('myresume/list_categories.html')
def show_categories(cat_selected=0):
    cats = Category.objects.all()
    return {'cats': cats, 'cat_selected': cat_selected}