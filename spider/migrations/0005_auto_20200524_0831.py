# Generated by Django 3.0.6 on 2020-05-24 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spider', '0004_auto_20200524_0816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='results',
            name='email',
            field=models.EmailField(max_length=128),
        ),
    ]
