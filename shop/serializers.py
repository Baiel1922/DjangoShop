from rest_framework import serializers


from .models import Brand, Category, Season, Gender, Product,\
    ProductImage, Favorite, ProductChildren, ProductChildrenImage

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = '__all__'

class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = ProductImageSerializer(instance.images.all(),
                                                          context=self.context,
                                                          many=True).data
        representation['product_children'] = ProductChildrenSrializer(instance.product_children.all(),
                                                                      context=self.context,
                                                                      many=True).data

        return representation

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'

class ProductChildrenImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductChildrenImage
        fields = '__all__'

class ProductChildrenSrializer(serializers.ModelSerializer):
    class Meta:
        model = ProductChildren
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = ProductChildrenImageSerializer(instance.images.all(),
                                                          context=self.context,
                                                          many=True).data
        return representation

class FavoriteSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Favorite
        fields = '__all__'
        # extra_kwargs = {
        #     'product': {'write_only': True},
        # }
    def create(self, validated_data):
        request = self.context.get('request')
        product = validated_data.get('product')
        user = request.user
        favorite, _ = Favorite.objects.get_or_create(user=user, product=product)
        print(favorite, _)
        return favorite

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['product_detail'] = ProductSerializer(Product.objects.get(id=instance.product.id),
                                                          context=self.context,
                                                          many=False).data
        return representation
