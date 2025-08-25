from rest_framework import generics, permissions
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Post
from .serializers import PostSerializer

# Create a new post
class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# List all posts (optional, not the feed)
class PostListView(generics.ListAPIView):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

# Feed view – posts from followed users
class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # All users the current user is following
        following_users = self.request.user.following.all()
        # Get posts by those users, newest first
        return Post.objects.filter(author__in=following_users).order_by("-created_at")

# Test endpoint
def index(request):
    return JsonResponse({"message": "Posts app is working!"})
