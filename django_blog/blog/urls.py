# blog/urls.py
from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

urlpatterns = [
    # Home (Post List)
    path("", PostListView.as_view(), name="home"),

    # Auth URLs
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),

    # Post CRUD
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]

from .views import CommentCreateView, CommentUpdateView, CommentDeleteView

urlpatterns += [
    path('post/<int:pk>/comment/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]

from django.urls import path
from . import views

urlpatterns = [ 
    path('search/', views.search_posts, name='search_posts'),
    path('tags/<slug:tag_slug>/', views.posts_by_tag, name='posts_by_tag'),  # For tag filter view
]

from django.urls import path
from . import views

urlpatterns = [
    # Existing paths
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    
    # Add this line for creating a new comment
    path('post/<int:pk>/comments/new/', views.add_comment, name='add_comment'),
]
