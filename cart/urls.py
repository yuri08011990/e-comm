from django.conf.urls import url
from . import views
from django.urls import include, path, re_path

app_name = 'cart'

urlpatterns = [
    re_path(r'^remove/(?P<product_id>\d+)/$', views.CartRemove, name='CartRemove'),
    re_path(r'^add/(?P<product_id>\d+)/$', views.CartAdd, name='CartAdd'),
    re_path(r'^$', views.CartDetail, name='CartDetail'),
]