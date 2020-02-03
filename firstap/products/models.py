from django.db import models
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django.urls import reverse

# Create your models here.
class Product(models.Model):
	name		= models.CharField(max_length = 50, blank=True) #blank true значит поле может быть пустым
	title   	= models.CharField(max_length = 120) #необходимо указать длину max_length
	description = models.TextField(blank = True, null = True)
	price 		= models.DecimalField(decimal_places = 2, max_digits = 10000, null = True, blank = True)
	summary		= models.TextField(blank = False, null = False)
	featured    = models.BooleanField() # null = True, default = True
	img 		= models.TextField(max_length=500, blank=True) 

	def __str__(self):
		return self.name #переименовывает объект в более удобный формат в админке( title )

	def get_absolute_url(self):

		return reverse('detail', kwargs={"id": self.id}) #позволяет создавать страницу при переходе на продукт

# class Article(models.Model):
# 	title	= models.CharField(max_length = 150)

	# class OtherInfo (models.Model):
	# 	name	= models.CharField(max_length = 100)

