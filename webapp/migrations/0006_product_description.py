# Generated by Django 3.1.7 on 2021-03-31 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_auto_20210331_1750'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=150, null=True),
        ),
    ]