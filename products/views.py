from django.shortcuts import render
from django.views.generic import ListView,DetailView

from.models import Product, Brand
# from . import forms

# Create your views here.
class ProductList(ListView):
    model = Product
    
class ProductDetail(DetailView):
     model = Product 

def get_context_data(self,  **kwargs):
        context = super().get_context_data( **kwargs)
        myproduct=self.get_objects() 
        context["images"] = ProductImages.objects.filter(product=myproduct) 
        context["related"] = Product.objects.filter(category=myproduct.category)       
        return context
     
class BrandList(ListView):
      model = Brand

      def get_context_data(self,  **kwargs):
        context = super().get_context_data( **kwargs)
        brand=self.get_objects()  
        context["brand_products"] = Product.objects.filter(brand=brand)       
        return context
  