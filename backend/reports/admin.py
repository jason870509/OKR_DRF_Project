from django.contrib import admin
from .models import Report, Category

class ReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author',
                    'category', 'create_at')
    list_display_links = ('id', 'title')
    list_filter = ('author',)
    list_per_page = 25


admin.site.register(Report, ReportAdmin)
admin.site.register(Category)

