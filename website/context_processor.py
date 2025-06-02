from solutions.models import Solution
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
            4: products.filter(product_type=4),
            5: products.filter(product_type=5),
        }
    }

def customer_menu(request):
    customers = Solution.objects.filter(
        is_published=True,
        solution_type=2
    ).distinct()
    return {
        'menu_customers': customers
    }