# Generated by Django 4.2.3 on 2023-08-29 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_masters'),
    ]

    operations = [
        migrations.AlterField(
            model_name='masters',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
    ]
