from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count, Q
from django.http import Http404, HttpResponseRedirect
from django.views import View
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator

from . import forms
from .models import Solution, SolutionCategory


class SolutionListView(ListView):
    queryset = Solution.objects.filter(is_published=True)
    template_name = 'website/solution.html'
    context_object_name = 'solutions'
    paginate_by = 5

    def get_queryset(self):
        cat = self.request.GET.get('cat')
        search = self.request.GET.get('search')
        solution_type = self.request.GET.get('solution_type')
        queryset = self.queryset
        if cat:
            queryset = queryset.filter(categories__slug=cat)
        if search:
            queryset = queryset.filter(content__icontains=search)
        if solution_type:
            queryset = queryset.filter(solution_type=solution_type)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['solution_type'] = self.request.GET.get('solution_type')
        return context


class SolutionDetailView(DetailView):
    queryset = Solution.objects.filter(is_published=True)
    template_name = 'website/solution_details.html'
    context_object_name = 'solution'

    def get_queryset(self):
        # cat = self.request.GET.get('cat')
        # search = self.request.GET.get('search')
        solution_type = self.request.GET.get('solution_type')
        queryset = self.queryset
        # if cat:
        #     queryset = queryset.filter(categories__slug=cat)
        # if search:
        #     queryset = queryset.filter(content__icontains=search)
        if solution_type:
            queryset = queryset.filter(solution_type=solution_type)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['solution_type'] = self.request.GET.get('solution_type')
        context['solution_categories'] = SolutionCategory.objects.filter(is_active=True)
        context['recent_posts'] = Solution.objects.filter(is_published=True).order_by('-created_at')
        return context