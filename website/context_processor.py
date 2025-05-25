from products.models import Product
from customers.models import Customer

def navbar_context(request):
    products = Product.objects.filter(is_published=True)
    return {
        'product_sections': {
            0: products.filter(product_type=0),
            1: products.filter(product_type=1),
            2: products.filter(product_type=2),
            3: products.filter(product_type=3),
        }
    }

def customer_menu(request):
    return {
        'menu_customers': Customer.objects.filter(is_published=True)
    }