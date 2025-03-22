from django.contrib import admin
from .models import Vacancy, GeminiResult, GeminiPrompt, TaskQueue, ExchangeRate
from simple_history.admin import SimpleHistoryAdmin

admin.site.register(GeminiResult)
admin.site.register(GeminiPrompt, SimpleHistoryAdmin)  # Регистрируем модель GeminiPrompt

@admin.register(ExchangeRate)
class ExchangeRateAdmin(admin.ModelAdmin):
    list_display = ('currency', 'rate', 'updated_at')
    readonly_fields = ('updated_at',)
    search_fields = ('currency',)

@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('company', 'geo', 'specialization', 'grade', 'date_posted', 'source', 'salary_min', 'salary_max',
                    'currency', 'work_format', 'bonus', 'bonus_conditions', 'author')

    search_fields = ('company', 'specialization', 'author', 'grade', 'date_posted', 'source', 'currency', 'geo')
    list_filter = ('company', 'specialization', 'author', 'grade', 'date_posted', 'source', 'currency', 'geo')