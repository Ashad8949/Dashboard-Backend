# Generated by Django 4.2.10 on 2024-02-09 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard_app', '0012_alter_insight_end_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insight',
            name='start_year',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
