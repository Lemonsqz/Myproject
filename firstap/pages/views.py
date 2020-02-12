from django.shortcuts import render, get_object_or_404
from products.models import *
from django.views import generic
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.utils import timezone

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



class ProductView(ListView):
 	model = Product
 	template_name = "products.html"

class ProductDetailView(DetailView):
	model = Product
	template_name = "product/detail.html"



def dynamic_lookup_view(request, id):
	obj = Product.objects.get(id=id)
	context = {
		"object": obj
	}

	return render(request, 'product/detail.html', context )


def add_to_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    order_item, created = OrderProduct.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]

        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated.")

        else:
            order.items.add(order_item)
            messages.info(request, "This item was added in your cart.")

    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "This item was added in your cart.")

    return redirect("detail", slug=slug)




def remove_from_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
        )
    if order_qs.exists():
        order = order_qs[0]

        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderProduct.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order_item.delete()
                messages.info(request, "This item was removed.")
        else:
            messages.info(request, "This item was not in your cart.")
            return redirect("detail", slug=slug)

    else:
        messages.info(request, "You don't have an active order.")

        return redirect("detail", slug=slug)
    return redirect("detail", slug=slug)