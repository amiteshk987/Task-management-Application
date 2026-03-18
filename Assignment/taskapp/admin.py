from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'due_date', 'created_by')
    list_filter = ('status', 'created_on')
    search_fields = ('title', 'description')
    readonly_fields = ('created_on', 'last_updated_on')
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.last_updated_by = request.user
        super().save_model(request, obj, form, change)