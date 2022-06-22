from django.contrib import admin
from menucode.forms import CategoryForm
from menucode.models import Product, Category

# Register your models here.
class SuperUserAdmin(admin.ModelAdmin):
    readonly_fields = ('createdAt', 'updatedAt')
    
            
   
admin.site.register(Product, SuperUserAdmin)
admin.site.register(Category, SuperUserAdmin)