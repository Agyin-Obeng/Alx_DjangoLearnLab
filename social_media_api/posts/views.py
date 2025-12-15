from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer


class FeedView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.request.user
        following_users = user.following.all()

        return Post.objects.filter(
            author__in=following_users
        ).order_by("-created_at")
