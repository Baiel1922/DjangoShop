from rest_framework import serializers
from .models import CartItem
from shop.serializers import ProductSerializer
from shop.models import Product, ProductChildren
from django.shortcuts import get_object_or_404

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    product_children_data = serializers.SerializerMethodField()

    class Meta:
        model = CartItem
        fields = ['user', 'product', 'quantity', 'product_children_data']

    def get_product_children_data(self, obj):
        product_children = obj.product_children
        product_children_data = {
            'id': product_children.id,
            'color': product_children.color.name,
            'size': product_children.size.name,
            'quantity': product_children.quantity,
            'is_available': product_children.is_available,
        }
        return product_children_data


class CartItemAddSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = CartItem
        fields = '__all__'
        # extra_kwargs = {
        #     'quantity': {'required': True},
        #     'product_id': {'required': True},
        # }

    def create(self, validated_data):
        user = self.context.get('request').user
        product = get_object_or_404(Product, id=validated_data['product'].id)
        item_quantity = validated_data.get('quantity')
        product_children = get_object_or_404(ProductChildren, id=validated_data['product_children'].id)
        if product.is_available is False or \
                product_children.is_available is False or \
                product_children.quantity < validated_data['quantity'] or \
                not product_children.product_parent.id == product.id:
                    raise serializers.ValidationError(
                        {'not available': 'the product is not available.'})

        try:
            cart_item = CartItem.objects.get(
                product=product,
                user=user,
                product_children=product_children,
            )
            cart_item.quantity += item_quantity
            cart_item.add_amount(item_quantity)
        except:
            cart_item = CartItem.objects.create(
                product=product,
                product_children=product_children,
                user=user,
                quantity=item_quantity
                )
            cart_item.add_amount(item_quantity)

        cart_item.save()
        product_children.quantity -= item_quantity
        product_children.save()
        product.save()
        return cart_item