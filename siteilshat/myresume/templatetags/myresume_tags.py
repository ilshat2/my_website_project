from django import template
from django.db.models import Count
#import myresume.views as views
from myresume.models import TagPost, Category

register = template.Library()


@register.inclusion_tag('myresume/list_categories.html')
def show_categories(cat_selected=0):
    cats = Category.objects.annotate(total=Count('posts')).filter(total__gt=0)
    return {'cats': cats, 'cat_selected': cat_selected}

@register.inclusion_tag('myresume/list_tags.html')
def show_all_tags():
    return {'tags': TagPost.objects.annotate(total=Count('tags')).filter(total__gt=0)}
