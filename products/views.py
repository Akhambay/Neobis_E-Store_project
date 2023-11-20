from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


@api_view(['POST'])
def calculate_total_price(request):
    data = request.data
    product_ids = data.get('product_ids', [])
    quantities = data.get('quantities', [])

    total_price = 0

    for product_id, quantity in zip(product_ids, quantities):
        try:
            product = Product.objects.get(pk=product_id)
            total_price += product.price * quantity
        except Product.DoesNotExist:
            return Response({'error': f'Product with id {product_id} not found'}, status=404)

    return Response({'total_price': total_price})
