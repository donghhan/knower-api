# Generated by Django 4.2.7 on 2023-11-25 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_knoweruser_is_active_knoweruser_is_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='knoweruser',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='활동 여부'),
        ),
    ]
