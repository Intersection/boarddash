from django.contrib import admin

from .models import NYC311Record, CommunityBoard

admin.site.register(NYC311Record)
admin.site.register(CommunityBoard)
