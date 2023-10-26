from django.contrib import admin
from .models import Profile
# Register your models here.



class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'