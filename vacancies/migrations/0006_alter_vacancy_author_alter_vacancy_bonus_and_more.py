# Generated by Django 4.2.20 on 2025-03-15 18:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vacancies', '0005_taskqueue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='author',
            field=models.CharField(blank=True, max_length=255, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='bonus',
            field=models.CharField(blank=True, max_length=255, verbose_name='Бонус'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='bonus_conditions',
            field=models.CharField(blank=True, max_length=255, verbose_name='Описание бонуса'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='company',
            field=models.CharField(max_length=255, verbose_name='Компания'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='currency',
            field=models.CharField(max_length=50, verbose_name='Валюта'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='date_posted',
            field=models.DateField(verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='geo',
            field=models.CharField(max_length=255, verbose_name='Локация'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='grade',
            field=models.CharField(max_length=255, verbose_name='Грейд'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='gross_net',
            field=models.CharField(max_length=50, verbose_name='Gross/Net'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='salary_max',
            field=models.IntegerField(blank=True, null=True, verbose_name='Max'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='salary_min',
            field=models.IntegerField(blank=True, null=True, verbose_name='Min'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='source',
            field=models.CharField(blank=True, max_length=255, verbose_name='Источник'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='specialization',
            field=models.CharField(max_length=255, verbose_name='Специализация'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='work_format',
            field=models.CharField(max_length=255, verbose_name='Формат работы'),
        ),
        migrations.CreateModel(
            name='HistoricalGeminiPrompt',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('prompt_text', models.TextField(verbose_name='Промпт для Gemini AI')),
                ('updated_at', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical gemini prompt',
                'verbose_name_plural': 'historical gemini prompts',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
