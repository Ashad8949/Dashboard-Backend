# Generated by Django 4.2.10 on 2024-02-09 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard_app', '0009_alter_insight_country_alter_insight_pestle_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insight',
            name='source',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
