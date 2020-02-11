from django.db import models
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django.urls import reverse
from django.conf import settings
from django.shortcuts import reverse

# Create your models here.

CATEGORY_CHOICES = (
	('D', 'Devices'),
	('O', 'Others'),
	('A', 'Accessory')
)




class Product(models.Model):
	name		= models.CharField(max_length = 50, blank=True) #blank true значит поле может быть пустым
	title   	= models.CharField(max_length = 120) #необходимо указать длину max_length
	description = models.TextField(blank = True, null = True)
	price 		= models.DecimalField(decimal_places = 2, max_digits = 10000, null = True, blank = True)
	summary		= models.TextField(blank = False, null = False)
	category 	= models.CharField(choices=CATEGORY_CHOICES, max_length = 1 )
	featured    = models.BooleanField() # null = True, default = True
	img 		= models.TextField(max_length=500, blank=True) 
	slug 		= models.SlugField()

	def __str__(self):
		return self.name #переименовывает объект в более удобный формат в админке( title )

	def get_absolute_url(self):

		return reverse("detail", kwargs={
			'slug': self.slug
		}) #позволяет создавать страницу при переходе на продукт

# class Article(models.Model):
# 	title	= models.CharField(max_length = 150)

	# class OtherInfo (models.Model):
	# 	name	= models.CharField(max_length = 100)

class OrderProduct(models.Model):
<<<<<<< HEAD
<<<<<<< HEAD
	user = models.ForeignKey(settings.AUTH_USER_MODEL,
								on_delete=models.CASCADE, blank=True, null=False)
	ordered = models.BooleanField(default=False)
=======
>>>>>>> parent of fe8e3b8... доб модель и вьюха корзины
=======
>>>>>>> parent of fe8e3b8... доб модель и вьюха корзины
	item = models.ForeignKey(Product, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Order(models.Model):
<<<<<<< HEAD
	# user = models.ForeignKey(settings.AUTH_USER_MODEL,
	# 						 on_delete=models.CASCADE, blank=True, null=True)
=======
	user = models.ForeignKey(settings.AUTH_USER_MODEL,
							 on_delete=models.CASCADE)
<<<<<<< HEAD
>>>>>>> parent of fe8e3b8... доб модель и вьюха корзины
=======
>>>>>>> parent of fe8e3b8... доб модель и вьюха корзины
	items = models.ManyToManyField(OrderProduct)
	start_date = models.DateTimeField(auto_now_add=True)
	ordered_date = models.DateTimeField()
	ordered = models.BooleanField(default=False)

	def __str__(self):
		return self.user.username