# Generated by Django 3.0.3 on 2020-06-27 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HappyHomesAdmin', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='residence_type',
            name='residence_id',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='residence_id',
        ),
        migrations.DeleteModel(
            name='Facility',
        ),
        migrations.DeleteModel(
            name='Residence',
        ),
        migrations.DeleteModel(
            name='Residence_type',
        ),
    ]
