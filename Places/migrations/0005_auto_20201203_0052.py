# Generated by Django 3.1.4 on 2020-12-02 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Places', '0004_placestovisit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='placestovisit',
            old_name='infos',
            new_name='info',
        ),
    ]
