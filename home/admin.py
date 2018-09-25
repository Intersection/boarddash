from django.contrib import admin

from .models import NYC311Record, CommunityBoard, BudgetRequest

admin.site.register(NYC311Record)
admin.site.register(CommunityBoard)
admin.site.register(BudgetRequest)
