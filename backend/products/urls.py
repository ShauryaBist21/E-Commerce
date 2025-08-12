from django.urls import path
from .views import (
    CategoryListView, CategoryDetailView,
    ProductListView, ProductDetailView, FeaturedProductsView,
    CartView, AddToCartView, UpdateCartItemView, RemoveFromCartView,
    OrderListView, OrderCreateView, OrderDetailView
)

urlpatterns = [
    # Category URLs
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<slug:slug>/', CategoryDetailView.as_view(), name='category-detail'),
    
    # Product URLs
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/featured/', FeaturedProductsView.as_view(), name='featured-products'),
    path('products/<slug:slug>/', ProductDetailView.as_view(), name='product-detail'),
    
    # Cart URLs
    path('cart/', CartView.as_view(), name='cart'),
    path('cart/add/', AddToCartView.as_view(), name='add-to-cart'),
    path('cart/update/<int:pk>/', UpdateCartItemView.as_view(), name='update-cart-item'),
    path('cart/remove/<int:pk>/', RemoveFromCartView.as_view(), name='remove-from-cart'),
    
    # Order URLs
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('orders/create/', OrderCreateView.as_view(), name='order-create'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
]
