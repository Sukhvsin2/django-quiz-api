# Generated by Django 3.1.3 on 2020-11-17 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qv1', '0003_auto_20201117_1813'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Questions',
            new_name='Question',
        ),
    ]