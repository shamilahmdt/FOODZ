# Generated by Django 5.1.7 on 2025-06-05 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_foodcategory_fooditem'),
    ]

    operations = [
        migrations.AddField(
            model_name='fooditem',
            name='restaurant',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
