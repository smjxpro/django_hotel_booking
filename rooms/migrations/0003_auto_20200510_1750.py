# Generated by Django 3.0.6 on 2020-05-10 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_auto_20200510_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomtype',
            name='ratings',
            field=models.DecimalField(decimal_places=1, max_digits=1),
        ),
    ]
