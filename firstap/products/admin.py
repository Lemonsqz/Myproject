from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

from .models import Product




class ProductAdmin(SummernoteModelAdmin):
	summernote_fields = ('img', 'title', 'description' )
	

admin.site.register(Product, ProductAdmin)