from django.urls import path
from .views import ProductList, ProductDetail, calculate_total_price

urlpatterns = [
    path("<int:pk>/", ProductDetail.as_view(), name="product_detail"),
    path("", ProductList.as_view(), name="product_list"),
    path('order/', calculate_total_price,
         name='order'),
]
