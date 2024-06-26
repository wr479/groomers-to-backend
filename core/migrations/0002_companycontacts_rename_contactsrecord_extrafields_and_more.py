# Generated by Django 4.2.3 on 2023-07-11 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyContacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('phone', models.CharField(max_length=16, verbose_name='Телефон')),
                ('requisites', models.TextField(verbose_name='Реквизиты')),
                ('address', models.CharField(max_length=128, verbose_name='Адрес')),
                ('address_html_code', models.TextField(verbose_name='HTML код для вставки карты')),
            ],
            options={
                'verbose_name': 'Контакты компании',
                'verbose_name_plural': 'Контакты компании',
            },
        ),
        migrations.RenameModel(
            old_name='ContactsRecord',
            new_name='ExtraFields',
        ),
        migrations.AlterModelOptions(
            name='extrafields',
            options={'verbose_name': 'Дополнительное поле', 'verbose_name_plural': 'Дополнительные поля'},
        ),
    ]
