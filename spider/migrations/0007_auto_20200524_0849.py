# Generated by Django 3.0.6 on 2020-05-24 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spider', '0006_auto_20200524_0845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='results',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
