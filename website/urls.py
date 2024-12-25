from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('services/', views.ServiceListView.as_view(), name='services'),
    path('page/<str:path>/', views.PageView.as_view(), name='page-view'),
]
# urlpatterns += admin_urls.urlpatterns
