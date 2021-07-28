# Generated by Django 3.1.1 on 2021-07-05 07:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('propertybuy', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('about', models.CharField(max_length=250)),
                ('pro_img', models.ImageField(blank=True, upload_to='propertyimage')),
                ('pro_img2', models.ImageField(blank=True, default='0', upload_to='propertyimage')),
                ('pro_img3', models.ImageField(blank=True, default='0', upload_to='propertyimage')),
                ('pro_img4', models.ImageField(blank=True, default='0', upload_to='propertyimage')),
                ('pro_img5', models.ImageField(blank=True, default='0', upload_to='propertyimage')),
                ('state', models.CharField(max_length=100)),
                ('city', models.CharField(blank=True, max_length=50)),
                ('full_address', models.CharField(max_length=200)),
                ('pincode', models.IntegerField()),
                ('bhk', models.CharField(max_length=40)),
                ('price', models.CharField(max_length=40)),
                ('date', models.DateTimeField(auto_now=True)),
                ('pro_type', models.CharField(max_length=20)),
                ('mobile', models.CharField(max_length=20)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='propertybuy.userproile')),
            ],
        ),
        migrations.CreateModel(
            name='chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Message', models.TextField()),
                ('Seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.propertydetails')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='addmorePro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_img2', models.ImageField(blank=True, upload_to='propertyimage')),
                ('pro_img3', models.ImageField(blank=True, upload_to='propertyimage')),
                ('pro_img4', models.ImageField(blank=True, upload_to='propertyimage')),
                ('pro_img5', models.ImageField(blank=True, upload_to='propertyimage')),
                ('propertyimage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.propertydetails')),
            ],
        ),
    ]
