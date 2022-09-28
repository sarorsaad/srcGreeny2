from django.contrib import admin
from .models import Product
# from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
# class HospitalModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
#     summernote_fields = '__all__'


admin.site.register(Product)
