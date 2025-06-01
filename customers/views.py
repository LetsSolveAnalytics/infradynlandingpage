from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count, Q
from django.http import Http404, HttpResponseRedirect
from django.views import View
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator

from . import forms
from .models import Customer, CustomerFeature, CustomerProductCategory
from coreapp.models import Testimonials, FAQ
from blogs.models import Post


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

class CustomerDetailView(DetailView):
    queryset = Customer.objects.filter(is_published=True)
    template_name = 'website/customer_details.html'
    context_object_name = 'customer'

    def get_queryset(self):
        # cat = self.request.GET.get('cat')
        # search = self.request.GET.get('search')
        customer_type = self.request.GET.get('customer_type')
        queryset = self.queryset
        # if cat:
        #     queryset = queryset.filter(categories__slug=cat)
        # if search:
        #     queryset = queryset.filter(content__icontains=search)
        # if customer_type:
        #     queryset = queryset.filter(customer_type=customer_type)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['testimonials'] = Testimonials.objects.filter(is_active=True)
        context['testimonial_intro'] = "What Our Clients Say!"
        context['faqs'] = FAQ.objects.filter(is_active=True)
        context['faq_intro'] = "Here are some of the most common questions we receive from our customers."
        context['customer_product_categories'] = CustomerProductCategory.objects.filter(is_active=True)
        context['customer_feature_intro'] = "Outperform yesterday. Everyday!"
        context['customer_feature_intro_content'] = "Your business is already a success. Procore can help you continue to grow—more reliably, with less risk and at a reduced cost."
        context['customer_features'] = CustomerFeature.objects.filter(is_active=True)
        context['recent_posts'] = Post.objects.filter(is_published=True).order_by('-created_at')[:6]
        return context