# Generated by Django 4.0.8 on 2023-04-19 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_course_title'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categroy',
            new_name='Category',
        ),
    ]
