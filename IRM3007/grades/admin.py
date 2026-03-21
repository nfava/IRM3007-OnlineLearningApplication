from django.contrib import admin

from .models import Assignment

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'due_date')  # shows these in admin list
    list_filter = ('due_date',)

