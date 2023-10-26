from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import Group
from dashboard.models import Profile
from dashboard.admin import ProfileInline


# class ProfileInline(admin.StackedInline):
#     model = Profile
#     can_delete = False
#     verbose_name_plural = 'Profile'

class UserAdmin(BaseUserAdmin):
    form  = UserChangeForm
    add_form = UserCreationForm
    list_filter = ('is_admin',)
    list_display = ['email','is_admin',"first_name","last_name"]
    fieldsets = (
                ('main',{'fields':('email','first_name','last_name','password','gender','birthdate_day','birthdate_month','birthdate_year','phone_number')}),
                 ('permissons',{'fields':('is_active','is_admin','last_login')}),
                 )
    add_fieldsets = (
        ('main',{'fields':('email','first_name','last_name','phone_number','password','confirm_password','gender','birthdate_day','birthdate_month','birthdate_year')}),
    )
    search_fields = ('email',)
    ordering = ('first_name','last_name')
    filter_horizontal = ()
    inlines = [ProfileInline]  # Add the ProfileInline to the inlines attribute


admin.site.unregister(Group)
admin.site.register(User,UserAdmin)