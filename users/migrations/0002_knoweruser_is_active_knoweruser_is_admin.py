# Generated by Django 4.2.7 on 2023-11-25 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='knoweruser',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='비휴면 여부'),
        ),
        migrations.AddField(
            model_name='knoweruser',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name='어드민'),
        ),
    ]