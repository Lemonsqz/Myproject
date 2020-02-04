from django.shortcuts import render
from products.models import *
from django.views import generic
from django.views.generic import ListView, DetailView

# Create your views here.

def home_view(request):

	return render(request, 'index.html')

def about_view(request):
	obj = Product.objects.get(name='phone')

	my_context = {
		"all_items": Product.objects.all(),
		"phone": [obj.img, obj.price],
		"my_text": "This is information about us",
		"my_numb": "azino 777",
		"my_list": [123, 321, 'abc']
	}
	return render(request, 'about.html', my_context)

def contact_view(request):
	# obj = Product.objects.get(id=3)
	context = {
		# 'description':obj.description,
	}

	return render(request, 'contacts.html', context)

def products_view(request):
	context = {
		'obj': Product.objects.all()
	}

	return render(request, 'products.html', context )

# class ProductView(ListView):
# 	model = Product
# 	template_name = "products.html"

def dynamic_lookup_view(request, id):
	obj = Product.objects.get(id=id)
	context = {
		"object": obj
	}

	return render(request, 'product/detail.html', context )




	# 	obj = Product.objects.get(name = 'tin') #в качестве name  выступает название статьи статьи 
	# obj1 = Product.objects.get(name = 'refrigerator')
	# obj2 = Product.objects.get(name = 'phone')
	# context = {
	# 	'sum': obj.summary,
	# 	'img': obj.img,
	# 	'description': obj.description,
	# 	'price': obj.price,
	# 	'sum1': obj1.summary,
	# 	'img1': obj1.img,
	# 	'description1': obj1.description,
	# 	'price1': obj1.price,
	# 	'sum2': obj2.summary,
	# 	'img2': obj2.img,
	# 	'description2': obj2.description,
	# 	'price2': obj2.price
	# }