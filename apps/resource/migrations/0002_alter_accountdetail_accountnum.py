# Generated by Django 4.1.12 on 2024-04-23 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountdetail',
            name='accountnum',
            field=models.IntegerField(max_length=11),
        ),
    ]
