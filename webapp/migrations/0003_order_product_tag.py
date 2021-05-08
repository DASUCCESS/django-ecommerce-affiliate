# Generated by Django 3.1.7 on 2021-03-31 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_remove_customer_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fieldName', models.DateField(null=True)),
                ('last_name', models.CharField(max_length=50, null=True)),
                ('address', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('indoor', 'indoor'), ('outdoors', 'outdoors'), ('general', 'general')], max_length=150, null=True)),
            ],
        ),
    ]