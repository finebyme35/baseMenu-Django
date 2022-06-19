from django.utils import timezone
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from menucode.serializers import ProductSerializer
from menucode.forms import ProductForm
from menucode.models import Product

@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)




@api_view(['GET'])
@permission_classes([IsAdminUser])
def getProduct(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def createProduct(request):
    productForm = ProductForm()
    if request.method == 'POST':
        if productForm.is_valid():
            if request.price != None and request.name != None and request.category != None:
                product = Product.objects.create(
                category=request.category,
                name=request.name,
                price=request.price,
                description=request.description,
                )
                serializer = ProductSerializer(product, many=False)
                return Response(serializer.data)
            else:
                return Response("Ürünün fiyat,isim ve kategori bilgilerinin girilmesi zorunludur.")
        else:
            return Response("Girdiğiniz bilgileri tekrar kontrol ediniz!")
    


@api_view(['PUT', 'POST'])
@permission_classes([IsAdminUser])
def updateProduct(request, pk):
    product = Product.objects.get(id=pk)
    if request.price != None and request.name != None and request.category != None:
        product.name = request.name
        product.price = request.price
        product.category = request.category
        product.description = request.description
        product.save()
        serializer = ProductSerializer(product, many=False)
        return Response(serializer.data)
    else:
        return Response("Ürünün fiyat,isim ve kategori bilgilerinin girilmesi zorunludur.")


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return Response('Ürün silindi.')


@api_view(['POST'])
@permission_classes([IsAdminUser])
def uploadImage(request):
    data = request.data

    productid = data['id']
    product = Product.objects.get(id=productid)

    product.image = request.FILES.get('image')
    product.save()

    return Response('Resim yüklendi.')


