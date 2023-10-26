from django.contrib import admin
from .models import Products,Category
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
     prepopulated_fields = {'slug': ('name',)} 

admin.site.register(Category,CategoryAdmin)
admin.site.register(Products)