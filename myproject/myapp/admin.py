from django.contrib import admin
from myapp.models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'kpi', 'okrs', 'salary', 'updated', 'created')
    search_fields = ('name', 'kpi', 'okrs', 'salary')