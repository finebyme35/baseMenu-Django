from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from menucode.serializers import CategorySeriliazer
from menucode.forms import CategoryForm
from menucode.models import Category

@api_view(['GET'])
def getCategorys(request):
    categorys = Category.objects.all()
    serializer = CategorySeriliazer(categorys, many=True)
    return Response(serializer.data)




@api_view(['GET'])
@permission_classes([IsAdminUser])
def getCategory(request, pk):
    category = Category.objects.get(id=pk)
    serializer = CategorySeriliazer(category, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def createCategorys(request):
    categoryForm = CategoryForm()
    if request.method == 'POST':
        if categoryForm.is_valid():
            category = Category.objects.create(
                name=request.name, 
            )
            serializer = CategorySeriliazer(category, many=False)
            return Response(serializer.data)
        else:
            return Response("Girdiğiniz bilgileri tekrar kontrol ediniz!")
    


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateCategorys(request, pk):
    data = request.data
    category = Category.objects.get(id=pk)
    category.name = data['name']
    category.save()

    serializer = CategorySeriliazer(category, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteCategory(request, pk):
    category = Category.objects.get(id=pk)
    category.delete()
    return Response('Kategori silindi.')




