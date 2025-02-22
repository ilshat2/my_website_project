from django import template
#import myresume.views as views
from myresume.models import TagPost, Category

register = template.Library()


@register.inclusion_tag('myresume/list_categories.html')
def show_categories(cat_selected=0):
    cats = Category.objects.all()
    return {'cats': cats, 'cat_selected': cat_selected}

@register.inclusion_tag('myresume/list_tags.html')
def show_all_tags():
    return {'tags': TagPost.objects.all()}
