from django.contrib import admin
from .models import Operation


class OperationAdmin(admin.ModelAdmin):
    list_display = ['From', 'value', 'To', 'result', 'date', 'user_id']


admin.site.register(Operation, OperationAdmin)
