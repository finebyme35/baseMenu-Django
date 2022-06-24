from django import forms
from numpy import einsum
from .models import Product, Category
from rest_framework.response import Response
from django.db import IntegrityError, transaction
from menucode.serializers import CategorySeriliazer
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'category']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['id','name', 'placementId']

    
 

class CategoryAdminForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['id', 'name', 'placementId']
