# Generated by Django 3.1.7 on 2021-03-31 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(null=True),
        ),
    ]
