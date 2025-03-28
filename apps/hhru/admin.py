from django.contrib import admin
from apps.hhru.models import VacancyHH

@admin.register(VacancyHH)
class VacancyHHAdmin(admin.ModelAdmin):
    list_display = ('hh_id', 'title', 'salary_from', 'salary_to', 'currency', 'area', 'created_at')

    search_fields = ('hh_id', 'title', 'description', 'salary_from', 'salary_to', 'currency', 'area', 'created_at')
    list_filter = ('currency', 'area', 'created_at')