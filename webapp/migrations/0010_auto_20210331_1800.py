# Generated by Django 3.1.7 on 2021-03-31 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_auto_20210331_1754'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='fieldName',
            new_name='date_ordered',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='last_name',
            new_name='order_status',
        ),
    ]
