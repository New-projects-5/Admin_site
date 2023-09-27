from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'brand', 'image', 'type_choice', 'description', 'price', 'amount', 'created_time', 'updated_time']

        extra_kwargs = {
            "id": {"read_only": True},
            "created_time": {"read_only": True},
            "updated_time": {"read_only": True},
        }