from django.urls import path
from catalog.views import (
    gallery_detail_page,
    prestige
)
from . import views
from django.conf.urls import url



urlpatterns = [
    path('', views.index, name='index'),
    url(r'^weapons/$', views.BookListView.as_view(), name='weapons'),
    url(r'^weapon/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    url(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
    url(r'^author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),
    url(r'^testing/$', views.testing, name='testing'),
    url(r'^rifles/$', views.RifleListView.as_view(), name = 'rifles'),
    url(r'^rifle/(?P<pk>\d+)$', views.RifleDetailView.as_view(), name='rifles-detail'),
    url('gallery/', gallery_detail_page, name = 'gallery'),
    url('allweapons', views.weapons, name='allweapons'),
    url('prestige/', prestige, name = 'prestige'),
    ]
