# Generated by Django 3.0.3 on 2020-06-28 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HappyHomesAdmin', '0003_auto_20200627_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='residence',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
