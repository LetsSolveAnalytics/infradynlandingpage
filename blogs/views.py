from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponseRedirect
from django.views import View
from django.views.generic import ListView, DetailView

from . import forms
from .models import Post, Category, Comment


class PostListView(ListView):
    queryset = Post.objects.filter(is_published=True)
    template_name = 'website/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        cat = self.request.GET.get('cat')
        search = self.request.GET.get('search')
        post_type = self.request.GET.get('post_type')
        queryset = self.queryset
        if cat:
            queryset = queryset.filter(categories__slug=cat)
        if search:
            queryset = queryset.filter(content__icontains=search)
        if post_type:
            queryset = queryset.filter(post_type=post_type)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_type'] = self.request.GET.get('post_type')
        return context


class PostDetailView(DetailView):
    queryset = Post.objects.filter(is_published=True)
    template_name = 'website/post_details.html'
    context_object_name = 'post'

    def get_queryset(self):
        # cat = self.request.GET.get('cat')
        # search = self.request.GET.get('search')
        post_type = self.request.GET.get('post_type')
        print(post_type)
        queryset = self.queryset
        # if cat:
        #     queryset = queryset.filter(categories__slug=cat)
        # if search:
        #     queryset = queryset.filter(content__icontains=search)
        if post_type:
            queryset = queryset.filter(post_type=post_type)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_type'] = self.request.GET.get('post_type')
        context['categories'] = Category.objects.filter(is_active=True)
        context['recent_posts'] = Post.objects.filter(is_published=True).order_by('-created_at')
        return context



class AddCommentView(View):
    def post(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id)
            form = forms.CommentForm(data=request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.save()
                return HttpResponseRedirect(self.request.path_info)
        except ObjectDoesNotExist:
            raise Http404
