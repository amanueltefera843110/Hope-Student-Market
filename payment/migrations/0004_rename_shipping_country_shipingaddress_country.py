# Generated by Django 5.1.6 on 2025-03-18 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_rename_address1_shipingaddress_shipping_address1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shipingaddress',
            old_name='shipping_country',
            new_name='country',
        ),
    ]
