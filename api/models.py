from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class AgentProfile(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=25)
    email = models.EmailField(max_length=100)
    instagram = models.CharField(max_length=25)
    facebook = models.CharField(max_length=50)
    image = models.ImageField(upload_to='agents/', default='')
    about = models.TextField()


class Property(models.Model):

    property_type_choices = (
        ('H', 'House'),
        ('HL', 'Hotel'),
        ('R', 'Retail'),
        ('I', 'Industrial'),
        ('O', 'Office'),
        ('L', 'Land'),
    )

    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200, default='')
    district = models.CharField(max_length=200, default='')
    location = models.CharField(max_length=200, default=0)
    price = models.CharField(max_length=50, default=0)
    property_type = models.CharField(
        max_length=3, choices=property_type_choices, default=0)
    area = models.CharField(max_length=20, default=0)
    no_of_beds = models.IntegerField(default=0)
    no_of_baths = models.IntegerField(default=0)
    no_of_garages = models.IntegerField(default=0)
    rating = models.IntegerField(default=1)
    description = models.TextField(default=0)
    image_1 = models.ImageField(upload_to='properties/', default='')
    image_2 = models.ImageField(upload_to='properties/', default='')
    image_3 = models.ImageField(upload_to='properties/', default='')
    sold = models.BooleanField(default=False)
    agent = models.ForeignKey(
        AgentProfile, on_delete=models.CASCADE)


class Comment(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    date_added = models.DateField(auto_now_add=True)
    comment = models.TextField(max_length=500)
