"""rogue URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from pages.views import *
from products.views import *
from django.conf import settings
from django.conf.urls.static import static
from pages import views




urlpatterns = [
	
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', index_view, name='home'),
    path('about/', about_view, name='about' ),
    path('contact/', contact_view, name='contact' ),
    path('detail/<slug>/', ProductDetailView.as_view(), name='detail' ),
    path('create/', product_create_view, name='create' ),
    path('products/', ProductView.as_view(), name='products' ),
    path('summernote/', include('django_summernote.urls')),
    path('api_products/', ProductAPIView.as_view()),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart' ),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary' ),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart, name='remove-single-item-from-cart'),

    # path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)










# urlpatterns += [
# path('products/', include('products.urls')),
# ]

# from django.views.generic import RedirectView
# urlpatterns += [
#     path('', RedirectView.as_view(url='/products/', permanent=True)),
#   ]