# Generated by Django 5.1.7 on 2025-06-18 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0009_offer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='offer',
            old_name='coupon_code',
            new_name='coupen_code',
        ),
    ]
