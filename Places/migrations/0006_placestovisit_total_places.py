# Generated by Django 3.1.4 on 2020-12-02 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Places', '0005_auto_20201203_0052'),
    ]

    operations = [
        migrations.AddField(
            model_name='placestovisit',
            name='total_places',
            field=models.IntegerField(null=True),
        ),
    ]