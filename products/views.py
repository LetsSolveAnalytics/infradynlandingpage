from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count, Q
from django.http import Http404, HttpResponseRedirect
from django.views import View
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator

from . import forms
from .models import Product, ProductFeature, ProductUsage
from coreapp.models import Testimonials, FAQ


# class ProductListView(ListView):
#     queryset = product.objects.filter(is_published=True)
#     template_name = 'website/solution.html'
#     context_object_name = 'solutions'
#     paginate_by = 5
#
#     def get_queryset(self):
#         cat = self.request.GET.get('cat')
#         search = self.request.GET.get('search')
#         solution_type = self.request.GET.get('solution_type')
#         queryset = self.queryset
#         if cat:
#             queryset = queryset.filter(categories__slug=cat)
#         if search:
#             queryset = queryset.filter(content__icontains=search)
#         if solution_type:
#             queryset = queryset.filter(solution_type=solution_type)
#         return queryset
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['solution_type'] = self.request.GET.get('solution_type')
#         return context


class ProductDetailView(DetailView):
    queryset = Product.objects.filter(is_published=True)
    template_name = 'website/product_details.html'
    context_object_name = 'product'

    def get_queryset(self):
        # cat = self.request.GET.get('cat')
        # search = self.request.GET.get('search')
        product_type = self.request.GET.get('product_type')
        queryset = self.queryset
        # if cat:
        #     queryset = queryset.filter(categories__slug=cat)
        # if search:
        #     queryset = queryset.filter(content__icontains=search)
        if product_type:
            queryset = queryset.filter(product_type=product_type)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = context['product']
        context['testimonials'] = Testimonials.objects.filter(is_active=True)
        context['testimonial_intro'] = "What Our Clients Say!"
        context['product_usages'] = product.usages.filter(is_active=True)
        context['product_usage_intro'] = "Check out where can this product be used?"
        # context['product_features'] = ProductFeature.objects.filter(is_active=True)
        context['product_features'] = product.features.filter(is_active=True)
        return context