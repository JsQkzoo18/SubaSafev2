from rest_framework import serializers

from .models import Article
from applications.category.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'name',
        )

class ArticleSerializer(serializers.ModelSerializer):

    category = CategorySerializer()
    
    class Meta:
        model = Article
        fields = (
            'name',
            'description',
            'main_image',
            'image_1',
            'image_2',
            'image_3',
            'image_4',
            'is_active',
            'starting_bid',
            'current_bid',
            'category',
            'seller',
            'buyer',
            'watchers',
        )


class ArticleSerializerViewSet(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('__all__')
