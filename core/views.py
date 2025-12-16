from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Product, Category, CartItem
import json


def home(request):
    """Homepage with hero section"""
    featured_products = Product.objects.filter(featured=True)[:4]
    return render(request, 'home.html', {
        'featured_products': featured_products,
    })


def shop(request):
    """Shop page with product grid"""
    products = Product.objects.all()
    categories = Category.objects.all()
    
    category_slug = request.GET.get('category')
    selected_category = None
    
    if category_slug:
        products = products.filter(category__slug=category_slug)
        selected_category = Category.objects.filter(slug=category_slug).first()
    
    return render(request, 'shop.html', {
        'products': products,
        'categories': categories,
        'current_category': category_slug,
        'selected_category': selected_category,
    })


def product_detail(request, slug):
    """Individual product page"""
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'product_detail.html', {
        'product': product,
    })


def cart(request):
    """Cart page"""
    if not request.session.session_key:
        request.session.create()
    
    cart_items = CartItem.objects.filter(session_key=request.session.session_key)
    total = sum(item.total_price for item in cart_items)
    
    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total': total,
    })


@require_POST
def add_to_cart(request):
    """Add product to cart via AJAX"""
    if not request.session.session_key:
        request.session.create()
    
    data = json.loads(request.body)
    product_id = data.get('product_id')
    quantity = data.get('quantity', 1)
    
    product = get_object_or_404(Product, id=product_id)
    
    cart_item, created = CartItem.objects.get_or_create(
        session_key=request.session.session_key,
        product=product,
        defaults={'quantity': quantity}
    )
    
    if not created:
        cart_item.quantity += quantity
        cart_item.save()
    
    cart_count = CartItem.objects.filter(session_key=request.session.session_key).count()
    
    return JsonResponse({
        'success': True,
        'cart_count': cart_count,
        'message': f'{product.name} added to cart'
    })


def get_cart_count(request):
    """Get cart count for header badge"""
    if not request.session.session_key:
        return JsonResponse({'count': 0})
    
    count = CartItem.objects.filter(session_key=request.session.session_key).count()
    return JsonResponse({'count': count})
