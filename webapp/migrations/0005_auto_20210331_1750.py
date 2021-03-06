# Generated by Django 3.1.7 on 2021-03-31 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_customer_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.CharField(choices=[('LAPTOPS', 'LAPTOPS'), ('CLOTHING', 'CLOTHING'), ('GADGET', 'GADGET')], max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name_of_product',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='webapp.tag'),
        ),
    ]
