from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    fields = ['url', ('minutes','seconds'), 'start_time','is_done', 'title', 'code', 'header']
    readonly_fields = ['is_done', 'start_time', 'title', 'code', 'header']
    list_display = ('url', 'start_time', 'report', 'is_done', 'title', 'code', 'header')

