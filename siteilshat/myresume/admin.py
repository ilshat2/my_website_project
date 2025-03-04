from django.contrib import admin, messages
from myresume.models import Myresume, Category


@admin.register(Myresume)
class MyresumeAdmin(admin.ModelAdmin):
    list_display = ('title', 'time_create', 'is_published', 'cat', 'brief_info')
    list_display_links = ('title', )
    ordering = ['-time_create', 'title']
    list_editable = ('is_published', )
    list_per_page = 5
    actions = ['set_published', 'set_draft']

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
