from django.shortcuts import render
from .models import *
from .forms import ProductForm
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProductSerializer

#здесь создаем API 
class ProductAPIView(APIView):
	def get(self, request):
		products = Product.objects.all()
		serializer = ProductSerializer(products, many=True)
		return Response({'products': serializer.data})

def product_create_view(request):
	form = ProductForm(request.POST or None)
	if form.is_valid():
		form.save()
	#через shell можно выяснить тот или иной элемент , не забыть про импортацию модели, в словарь можно добавить любые данные модели
	# context = {
	# 	'title': obj.title,
	# 	'description': obj.description,
	# }
	context = {
		'form': form
	}

	return render(request, "product/product_create.html", context)

# def product_detail_view(request):
# 	obj = Product.objects.get(id=1)
# 	#через shell можно выяснить тот или иной элемент , не забыть про импортацию модели, в словарь можно добавить любые данные модели
# 	# context = {
# 	# 	'title': obj.title,
# 	# 	'description': obj.description,
# 	# }
# 	context = {
# 		'object': obj
# 	}

# 	return render(request, "product/detail.html", context)