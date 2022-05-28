from django.contrib import admin
from .models import *

admin.site.register(General)


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title',)}
    list_display = ('id', 'title', 'time_created', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_created')


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('name',)}
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(News, BlogAdmin)
admin.site.register(Category, CategoryAdmin)

