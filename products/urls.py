from django.urls import path
from .views import ProductList,ProductDetail,BrandList
# from django.views.generic import TemplateView

app_name='products'

urlpatterns = [
 path("", ProductList.as_view(), name="product_list"),  
 path("<pk>/", ProductDetail.as_view(), name="product_detail"),
 path("brands/", BrandList.as_view(), name="brand_list"),
]