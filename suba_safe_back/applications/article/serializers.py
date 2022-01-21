from rest_framework import serializers

from .models import Article
from applications.category.models import Category
from applications.category.serializers import CategorySerializer

# class CategorySerializer(serializers.ModelSerializer):
    # class Meta:
        # model = Category
        # fields = (
            # 'name',
        # )

class ArticleSerializer(serializers.ModelSerializer):

    category = CategorySerializer()
    
    class Meta:
        model = Article
        fields = (
            'name',
            'description',
            'main_image',
            'main_image_opt_text',
            'image_1',
            'image_1_opt_text',
            'image_2',
            'image_2_opt_text',
            'image_3',
            'image_3_opt_text',
            'image_4',
            'image_4_opt_text',
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
