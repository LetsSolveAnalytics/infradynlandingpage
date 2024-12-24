from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('page/<str:path>/', views.PageView.as_view(), name='page-view'),
]
# urlpatterns += admin_urls.urlpatterns
