# Generated by Django 5.1.6 on 2025-03-16 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='old_cart',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
