from django.contrib import admin

# Register your models here.

from .models import Task
"""Minimal registration of Models.
admin.site.register(Task)
"""

class TaskAdmin(admin.ModelAdmin):
    """Administration object for Task models.
    Defines:
     - fields to be displayed in list view (list_display)
    """
    list_display = ('description', 'status')
   
admin.site.register(Task, TaskAdmin)

