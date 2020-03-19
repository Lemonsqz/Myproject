from django.shortcuts import render, get_object_or_404
from products.models import *
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.views.generic import ListView, DetailView, View
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.utils import timezone

# Create your views here.

def index_view(request):
    obj = Product.objects.all()
    context = {
        'rdr': obj[4],
        'tm': obj[3],
        'gow': obj[2],
        'lou': obj[0],
    }

    return render(request, 'index.html', context)





class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):

        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object': order
            }
            return render(self.request, 'order_summary.html', context)
        except ObjectDoesNotExist:
            messages.error(self.request, "You don't have an active Order")
            return redirect("/")
        

def about_view(request):
	# obj = Product.objects.all()
	# my_context = {
 #    'get': obj[0].description,
 #    }


	return render(request, 'about.html')

def contact_view(request):
	# obj = Product.objects.get(id=)
	# context = {'test':obj,}
 #    {
	# 	# 'description':obj.description,
	# }

	return render(request, 'contacts.html',)



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

@login_required
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



@login_required
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
                return redirect("order-summary")
        else:
            messages.info(request, "This item was not in your cart.")
            return redirect("order-summary")

    else:
        messages.info(request, "You don't have an active order.")

        return redirect("order-summary")
    return redirect("order-summary")


@login_required
def remove_single_item_from_cart(request, slug):
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
            order_item.quantity -= 1
            order_item.save()
            messages.info(request, "This item was removed.")
            return redirect("order-summary")
        else:
            order_item.delete()
            messages.info(request, "This item was removed.")

    else:
        messages.info(request, "You don't have an active order.")

        return redirect("order_summary")
    return redirect("order_summary")