# Generated by Django 4.2.10 on 2024-02-09 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard_app', '0002_insight_delete_dataentry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insight',
            name='published',
            field=models.DateTimeField(null=True),
        ),
    ]
