# Generated by Django 4.2.10 on 2024-02-09 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard_app', '0015_alter_insight_sector'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insight',
            name='country',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='insight',
            name='published',
            field=models.DateTimeField(null=True),
        ),
    ]
