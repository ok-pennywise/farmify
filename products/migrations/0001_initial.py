# Generated by Django 5.1.1 on 2024-09-19 04:45

import django.db.models.deletion
import model_utils
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.CharField(default=model_utils.generate_id, max_length=20, primary_key=True, serialize=False)),
                ('url', models.ImageField(upload_to='product_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.CharField(default=model_utils.generate_id, max_length=20, primary_key=True, serialize=False)),
                ('created_on', models.DateTimeField(default=model_utils.aware_utcnow)),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('min_quantity', models.IntegerField(default=1)),
                ('max_quantity', models.IntegerField(default=10000)),
                ('stock', models.IntegerField(default=0)),
                ('in_stock', models.BooleanField(default=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.category')),
            ],
        ),
    ]
