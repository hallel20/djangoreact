# Generated by Django 4.1.7 on 2023-03-28 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_property_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='rating',
            field=models.IntegerField(default=1),
        ),
    ]