from gc import get_objects
from django.contrib import admin
from menucode.models import Product, Category
from rest_framework.response import Response
from menucode.serializers import CategorySeriliazer
from menucode.forms import CategoryAdminForm
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    exclude = ('createdAt', 'updatedAt')
    class Meta:
        model = Product

class CategoryAdmin(admin.ModelAdmin):
    exclude = ('createdAt', 'updatedAt')
    form = CategoryAdminForm
   
    class Meta:
        model = Category

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)