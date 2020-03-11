from django.conf.urls import url, include
from .views import get_products

urlpatterns = [
    url(r'^$', get_products, name='products')
]