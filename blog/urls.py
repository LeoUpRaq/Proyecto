from django.urls import path

from core.views import HomeView
from .views import  BlogDetailView, BlogListView,BlogListViewEven

app_name="blog"

urlpatterns = [
    path('<int:pk>/',BlogDetailView.as_view(), name="detail"),
    path('hoteles/',BlogListView.as_view(),name="hotel"),
    path('indx/',BlogListViewEven.as_view(), name="home")
      
]
