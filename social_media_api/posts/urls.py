from django.urls import path
from .views import PostCreateView, PostListView, FeedView, index

urlpatterns = [
    path('', index, name='index'),
    path('create/', PostCreateView.as_view(), name='create-post'),
    path('all/', PostListView.as_view(), name='all-posts'),
    path('feed/', FeedView.as_view(), name='feed'), 
]
