# Generated by Django 4.2 on 2024-04-18 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('care', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pharmmodels',
            name='pharm_image',
        ),
    ]