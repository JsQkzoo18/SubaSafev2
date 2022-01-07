from rest_framework.response import Response
from rest_framework import viewsets

from .models import Category

from .serializers import CategorySerializer

def is_valid(category_name):
    if category_name.isalpha():
        return True
    else:
        return False


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def create(self, request):

        serializer = CategorySerializer(data = request.data)
        serializer.is_valid(raise_exception=True)

        category_name = serializer.validated_data['name']

        try:
            category = Category.objects.get(name=category_name)

            if category:
                return Response({'Status': 'La categoría ya existe'})
        except Category.DoesNotExist:
            
            name = serializer.validated_data.get('name')

            if is_valid(name):
                category = Category.objects.create(
                    name = serializer.validated_data['name'],
                )
                return Response({'Status': 'La categoría ha sido creada exitosamente'})
            else:
                return Response({'Status': 'La categoría no debe contener números'})


