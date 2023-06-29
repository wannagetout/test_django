from django.contrib import admin

from .models import Tasks

@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'status', 'update_date',)
    search_fields = ('status', )
    list_filter = ('status', )
