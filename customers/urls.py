from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>/', views.CustomerDetailView.as_view(), name='customer-detail'),
]
