# Generated by Django 4.2.3 on 2023-09-05 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_yourmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yourmodel',
            name='category',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='yourmodel',
            name='phone',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='yourmodel',
            name='question',
            field=models.TextField(blank=True),
        ),
    ]