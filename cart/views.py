from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from .serializers import CartItemSerializer, CartItemAddSerializer
from .models import CartItem
from shop.models import Product, ProductChildren
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from account.models import Profile

class CartItemView(generics.ListAPIView):
    serializer_class = CartItemSerializer
    permission_classes = (IsAuthenticated, )
    # filter_backends = [filters.SearchFilter]
    # search_fields = [
    #     'product__name', 'product__description', 'product__category__name']


    def get_queryset(self):
        user = self.request.user
        return CartItem.objects.filter(user=user)


class CartItemAddView(generics.CreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemAddSerializer
    permission_classes = (IsAuthenticated, )


class CartItemDelView(generics.DestroyAPIView):
    permission_classes = (IsAuthenticated, )
    queryset = CartItem.objects.all()

    def delete(self, request, pk, format=None):
        user = request.user
        cart_item = CartItem.objects.filter(user=user)
        target_product = get_object_or_404(cart_item, pk=pk)
        product_children = get_object_or_404(ProductChildren, id=target_product.product_children.id)
        product_children.quantity = product_children.quantity + target_product.quantity
        target_product.substract_amount()
        product_children.save()
        target_product.delete()
        return Response(status=status.HTTP_200_OK, data={"detail": "deleted"})


class CartItemAddOneView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request, pk, format=None):
        user = request.user
        cart_item = CartItem.objects.filter(user=user)
        target_product = get_object_or_404(cart_item, pk=pk)
        product_children = get_object_or_404(ProductChildren, id=target_product.product_children.id)
        if product_children.quantity <= 0:
            return Response(
                data={
                    "detail": "this item is sold out try another one !",
                    "code": "sold_out"})

        target_product.quantity = target_product.quantity + 1
        product_children.quantity = product_children.quantity - 1
        profile = Profile.objects.get(user=user)
        profile.total_price += product_children.product_parent.price
        profile.save()
        product_children.save()
        target_product.save()
        return Response(
            status=status.HTTP_226_IM_USED,
            data={"detail": 'one object added', "code": "done"})


class CartItemReduceOneView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request, pk, format=None):
        user = request.user
        cart_item = CartItem.objects.filter(user=user)
        target_product = cart_item.get(pk=pk)
        product_children = get_object_or_404(ProductChildren, id=target_product.product_children.id)
        if target_product.quantity == 0:
            return Response(
                data={
                    "detail": "there is no more item like this in tour cart",
                    "code": "no_more"})

        target_product.quantity = target_product.quantity - 1
        product_children.quantity = product_children.quantity + 1
        profile = Profile.objects.get(user=user)
        profile.total_price -= product_children.product_parent.price
        profile.save()
        product_children.save()
        target_product.save()
        return Response(
            status=status.HTTP_226_IM_USED,
            data={
                "detail": 'one object deleted',
                "code": "done"
            })



