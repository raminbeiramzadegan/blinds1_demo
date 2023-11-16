from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser,AbstractUser
from .managers import UserManager
from django.utils import timezone
# def validate_birthdate(birthdate):
#     if birthdate > timezone.now().date():
#         raise ValidationError(
#             _('Birthdate cannot be in the future.')
#         )

  
class User(AbstractBaseUser):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    MONTH_CHOICES = (
        ('1', 'January'),
        ('2', 'February'),
        ('3', 'March'),
        ('4', 'April'),
        ('5', 'May'),
        ('6', 'June'),
        ('7', 'July'),
        ('8', 'August'),
        ('9', 'September'),
        ('10', 'October'),
        ('11', 'November'),
        ('12', 'December'),    )

    DAY_CHOICES = [(str(day), str(day)) for day in range(1, 32)]
    YEAR_CHOICES = [(str(year), str(year)) for year in range(1900, 2024)]
    email = models.EmailField(max_length=255,unique=True)
    is_admin = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=11,blank=True,null=True)
    username = None
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    birthdate_day = models.CharField(max_length=2, choices=DAY_CHOICES, null=True, blank=True, default=None)
    birthdate_month = models.CharField(max_length=2, choices=MONTH_CHOICES, null=True, blank=True, default=None)
    birthdate_year = models.CharField(max_length=4, choices=YEAR_CHOICES, null=True, blank=True, default=None)
    first_name = models.CharField(max_length=50,blank=True,null=True)
    last_name = models.CharField(max_length=100,blank=True,null=True)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    last_seen = models.DateTimeField(null=True)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']


    def __str__(self):
        return self.email
    

    


    def has_perm(self,perm,obj = None):
        return True

    def has_module_perms(self, app_label):
        return True 

    @property
    def is_staff(self):
        return self.is_admin

    @property
    def is_active(self):
        return self.is_active
    
    @property
    def is_active(self):
        return self.is_admin
    

    @property
    def is_authenticated(self):
        return True if self.is_active else False

    # def save(self, *args, **kwargs):
    #     if self.birthdate_day and self.birthdate_month and self.birthdate_year:
    #         birthdate = timezone.datetime(self.birthdate_year, self.birthdate_month, self.birthdate_day).date()
    #         self.birthdate = birthdate
    #     super().save(*args, **kwargs)

    # def clean(self):
    #     if self.birthdate_day and self.birthdate_month and self.birthdate_year:
    #         birthdate = timezone.datetime(self.birthdate_year, self.birthdate_month, self.birthdate_day).date()
    #         validate_birthdate(birthdate)