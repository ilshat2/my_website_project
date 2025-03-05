from django.contrib import admin, messages
from myresume.models import Myresume, Category


class PhotoFilter(admin.SimpleListFilter):
    title = 'Есть ли фото'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return [
            ('there_photo', 'Есть фото'),
            ('no_photo', 'Нет фото')
        ]
    def queryset(self, request, queryset):
        if self.value() == 'there_photo':
            return queryset.filter(photo__isnull=False)
        elif self.value() == 'no_photo':
            return queryset.filter(photo__isnull=True)


@admin.register(Myresume)
class MyresumeAdmin(admin.ModelAdmin):
    list_display = ('title', 'time_create', 'is_published', 'cat', 'brief_info')
    list_display_links = ('title', )
    ordering = ['-time_create', 'title']
    list_editable = ('is_published', )
    list_per_page = 5
    actions = ['set_published', 'set_draft']
    search_fields = ['title__startswith', 'cat__name']
    list_filter = [PhotoFilter, 'cat__name', 'is_published']

    @admin.display(description='Краткое описание', ordering='content')
    def brief_info(self, myresume: Myresume):
        return f'Описание {len(myresume.content)} символов.'

    @admin.display(description='Опубликовать выбранные записи')
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Myresume.Status.PUBLISHED)
        self.message_user(request, f'Изменено {count} записей.')

    @admin.display(description='Снять с публикации выбранные записи')
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Myresume.Status.DRAFT)
        self.message_user(request, f'{count} записей снято с публикации!', messages.WARNING)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    ordering = ['id']
