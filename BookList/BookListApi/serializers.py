from rest_framework import serializers
from .models import BookItem, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','slug','title']

class BookItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = BookItem
        fields = ['id','title','price','inventory','category','category_id']
        depth = 1