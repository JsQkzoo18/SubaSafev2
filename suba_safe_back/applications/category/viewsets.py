from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
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
    authentication_classes = (TokenAuthentication, JWTAuthentication)

    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    def get_permissions(self):
        # Si el método es LIST o RETRIEVE
        if(self.action =='create'):
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [AllowAny]
        #
        return [permission() for permission in permission_classes]

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


