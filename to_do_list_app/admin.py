from __future__ import unicode_literals

from django.contrib import admin

from .models import List_Object

# Register your models here.

class List(admin.TabularInline):
    model = List_Object

class ListAdmin(admin.ModelAdmin):
    list_display = ('post_date', 'content', 'archived')

    inLines = [
        List,
    ]

admin.site.register(
    List_Object, ListAdmin
)