# Generated by Django 3.2 on 2022-05-29 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='startdate',
            field=models.DateField(),
        ),
    ]
