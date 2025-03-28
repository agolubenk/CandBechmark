# Generated by Django 5.1.7 on 2025-03-27 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0004_remove_aidialoguemessage_dialogue_delete_aidialogue_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Если отключено, вакансия не будет учитываться в статистике и сводных таблицах', verbose_name='Учитывать в статистике'),
        ),
    ]
