# Generated by Django 3.1.1 on 2021-07-05 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0003_auto_20210705_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertydetails',
            name='bookPrice',
            field=models.CharField(default='2000.00', max_length=20),
        ),
    ]
