from django.contrib import admin
from .models import Project, Task
# Register your models here.

class TaskInLine(admin.TabularInline):
    model = Task
    extra = 1

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'start_date', 'end_date')
    inlines = [TaskInLine]


admin.site.register(Project,ProjectAdmin)
admin.site.register(Task)