from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('services/', views.ServiceListView.as_view(), name='services'),
    path('membership/', views.MembershipView.as_view(), name='membership'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('gallery/', views.GalleryListView.as_view(), name='gallery'),
    path('page/<str:path>/', views.PageView.as_view(), name='page-view'),
]