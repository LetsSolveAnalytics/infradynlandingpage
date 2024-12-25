from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post-list'),
    path('<slug:slug>/', views.PostDetailView.as_view(), name='post-detail'),
    path('comment/<int:post_id>/', views.AddCommentView.as_view(), name='add-comment'),
]
