from django.contrib import admin
from core.models import Task
# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status')