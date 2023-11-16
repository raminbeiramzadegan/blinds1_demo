from django.db import models
from accounts.models import User
from .canadian_zip_validator import validate_canadian_zip
from django.core.exceptions import ValidationError
import re


# Create your models here.

def validate_city(value):
    if not re.match(r'^[a-zA-Z ]+$', value):
        raise ValidationError('City name must contain only alphabetic characters and spaces.')

def validate_street_address(value):

    if not re.match(r'^[a-zA-Z0-9\s\-.,#]+$', value):
        raise ValidationError('Invalid street address. Use only alphanumeric characters, spaces, "-", ".", ",", and "#".')

class Profile(models.Model):
    PROVINCE = (
        ('AB','Alberta'),
        ('BC','British Columbia'),
        ('MB','Manitoba'),
        ('NB','New Brunswick'),
        ('NF','Newfoundland'),
        ('YT','Yukon'),
        ('NS','Nova Scotia'),
        ('ON','Ontario'),
        ('PE','Prince Edward Island'),
        ('QC','Quebec'),
        ('SK','Saskatchewan'),
        ('NU','Nunavut'),
        ('NT','Northwest Territories')


    )
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='profile')
    street_address = models.CharField(max_length=255, validators=[validate_street_address])
    city = models.CharField(max_length=255,validators=[validate_city])
    province = models.CharField(max_length=2, choices=PROVINCE, null=True, blank=True, default=None)
    zip_code = models.CharField(max_length=7, validators=[validate_canadian_zip])
    default_shipping_address = models.BooleanField(default=True)

   