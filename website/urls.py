from django.urls import path
from . import views
from blogs.views import PostListView

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('solutions/', views.SolutionListView.as_view(), name='solutions'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('request-a-demo/', views.RequestDemoView.as_view(), name='request_a_demo'),
    path('pricing/', views.PricingRequestView.as_view(), name='pricing'),
]