from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

from .models import *




class ProductAdmin(SummernoteModelAdmin):
	summernote_fields = ('img', 'title', 'description', 'trailer', 'add_img', )


	

admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(OrderProduct)