# Generated by Django 4.2.7 on 2023-11-29 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_knoweruser_is_superuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='knoweruser',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='이름'),
        ),
        migrations.AlterField(
            model_name='knoweruser',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='성'),
        ),
    ]
