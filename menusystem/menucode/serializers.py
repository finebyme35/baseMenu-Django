from rest_framework import serializers
from .models import Product, Category




class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategorySeriliazer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Category
        fields = '__all__'
    
    def get_products(self, obj):
        products = obj.product_set.all()
        serializers = ProductSerializer(products, many=True)
        return serializers.data