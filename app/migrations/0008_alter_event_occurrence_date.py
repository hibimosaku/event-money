# Generated by Django 4.0.2 on 2022-04-08 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_event_occurrence_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='occurrence_date',
            field=models.DateField(),
        ),
    ]
