from django.conf.urls import url
from django.urls import path, re_path
from shop.views import base_view, product_view, category_view
from . import views

app_name = 'shop'

urlpatterns = [
    re_path(r'^$', base_view, name='base'),
    re_path(r'^product/(?P<product_slug>[-\w]+)/$', product_view, name='product_detail'),
    re_path(r'^category/(?P<category_slug>[-\w]+)/$', category_view, name='category_detail'),
]