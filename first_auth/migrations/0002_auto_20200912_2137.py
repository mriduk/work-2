# Generated by Django 3.1.1 on 2020-09-12 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='readers',
            options={'verbose_name': 'Reader', 'verbose_name_plural': 'Readers'},
        ),
    ]
