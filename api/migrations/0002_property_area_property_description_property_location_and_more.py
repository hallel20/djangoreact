# Generated by Django 4.1.7 on 2023-03-20 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='area',
            field=models.CharField(default=0, max_length=20),
        ),
        migrations.AddField(
            model_name='property',
            name='description',
            field=models.TextField(default=0),
        ),
        migrations.AddField(
            model_name='property',
            name='location',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AddField(
            model_name='property',
            name='no_of_baths',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='property',
            name='no_of_beds',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='property',
            name='no_of_garages',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='property',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='property',
            name='property_type',
            field=models.CharField(choices=[('H', 'House'), ('HL', 'Hotel'), ('R', 'Retail'), ('I', 'Industrial'), ('O', 'Office'), ('L', 'Land')], default=0, max_length=3),
        ),
        migrations.AddField(
            model_name='property',
            name='rating',
            field=models.CharField(choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)], default=0, max_length=5),
        ),
    ]
