# Generated by Django 4.1.7 on 2023-03-26 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_property_sold'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='price',
            field=models.CharField(default=0, max_length=50),
        ),
    ]
