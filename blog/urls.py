from django.urls import path
from . import views

urlpatterns = [
    # Path for the blog index (homepage)
    path('', views.PostList.as_view(), name='home'),
    
    # Path for individual blog posts (using the primary key 'pk' for lookup)
    path('<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
]
