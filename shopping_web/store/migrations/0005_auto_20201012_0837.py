# Generated by Django 3.1.2 on 2020-10-12 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
    ]
