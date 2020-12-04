# Generated by Django 3.1.4 on 2020-12-02 19:42

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Places', '0006_placestovisit_total_places'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placestovisit',
            name='info',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=1000), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='placestovisit',
            name='links',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='placestovisit',
            name='names',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=60), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='placestovisit',
            name='photo_links',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), null=True, size=None),
        ),
    ]
