from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('services/', views.ServiceListView.as_view(), name='services'),
    path('membership/', views.MembershipView.as_view(), name='membership'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('gallery/', views.GalleryListView.as_view(), name='gallery'),
    path('page/<str:path>/', views.PageView.as_view(), name='page-view'),
    path('events/', views.EventListView.as_view(), name='events'),
    path('quran-classes/', views.QuranclassView.as_view(), name='quran-classes'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('donate/', views.DonateView.as_view(), name='donate'),
    path('history/', views.HistoryView.as_view(), name='history'),
]