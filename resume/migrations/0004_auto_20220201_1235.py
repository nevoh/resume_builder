# Generated by Django 3.1.7 on 2022-02-01 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_achievement_language_skill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]