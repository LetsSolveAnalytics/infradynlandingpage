from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, JsonResponse
from django.shortcuts import render
from django.forms import modelform_factory
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View, generic
from django.views.generic import TemplateView, ListView
import requests

from .models import Post, Category, Comment
from . import forms


from .constants import PageType
from .models import Slider, Service, Page


# Create your views here.

class HomeView(TemplateView):
    template_name = 'website/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sliders'] = Slider.objects.filter(is_active=True)
        context['services'] = Service.objects.filter(is_active=True)
        return context


class ServiceListView(ListView):
    queryset = Service.objects.filter(is_active=True)
    template_name = 'website/services.html'
    context_object_name = 'services'


class PageView(View):
    def get(self, request, path):
        try:
            page = Page.objects.get(url_path=path)
            return render(request, 'website/page.html', {'page': page})
        except ObjectDoesNotExist:
            raise Http404
        
class ContactView(View):
    def post(self, request, detail_id):
        try:
            post = Post.objects.get(id=detail_id)
            form = forms.CommentForm(data=request.POST)
            if form.is_valid():
                detail = form.save(commit=False)
                detail.post = post
                detail.save()   
                r = requests.post('https://api.web3forms.com/submit')
                if r.status_code==200:
                    return HttpResponseRedirect(self.request.path_info)
                else:
                    return HttpResponseRedirect(self.request.path_info)
        except ObjectDoesNotExist:
            raise Http404