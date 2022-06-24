from django.contrib import admin
from menucode.models import Product, Category
from rest_framework.response import Response
from menucode.serializers import CategorySeriliazer
from menucode.forms import CategoryAdminForm
from adminsortable2.admin import SortableAdminBase, SortableAdminMixin, SortableInlineAdminMixin, SortableTabularInline, SortableStackedInline
from semantic_admin import SemanticModelAdmin
class ProductAdmin(admin.ModelAdmin):
    exclude = ('createdAt', 'updatedAt')
    list_display = ('name', 'category', 'price')
    list_per_page = 10
    ordering=['id']
    class Meta:
        model = Product
class CategoryAdmin(SortableAdminMixin, SemanticModelAdmin, admin.ModelAdmin):
    exclude = ('createdAt', 'updatedAt')
    form = CategoryAdminForm
    list_display = ('name', 'placementId')
    list_per_page = 10


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
