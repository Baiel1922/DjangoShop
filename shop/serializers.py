from rest_framework.serializers import ModelSerializer

from .models import Brand, Category, Season, Gender, Product, ProductImage

class ColorSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class SizeSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class BrandSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SeasonSerializer(ModelSerializer):
    class Meta:
        model = Season
        fields = '__all__'

class GenderSerializer(ModelSerializer):
    class Meta:
        model = Gender
        fields = '__all__'

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = ProductImageSerializer(instance.images.all(),
                                                          context=self.context,
                                                          many=True).data
        return representation
class ProductImageSerializer(ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'
