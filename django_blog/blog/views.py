# blog/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

from .forms import RegisterForm
from .models import Post

def home(request):
    posts = Post.objects.all().order_by('-published_date')
    return render(request, 'blog/index.html', {'posts': posts})


def register(request):
    """
    Create a new user (username, email, password). On success, log the user in and redirect home.
    """
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful. You are now logged in.")
            return redirect('home')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = RegisterForm()
    return render(request, 'blog/register.html', {'form': form})


def login_view(request):
    """
    Uses Django's AuthenticationForm to log users in.
    """
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Logged in successfully.")
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials. Please try again.")
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})


def logout_view(request):
    """
    Log the user out and redirect to home.
    """
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('home')


@login_required
def profile(request):
    """
    Allow authenticated users to view and edit their profile (only email here).
    Handles GET and POST. Keeps things simple and consistent.
    """
    user = request.user

    if request.method == 'POST':
        # Update email (you can expand this to username, bio, avatar etc.)
        new_email = request.POST.get('email', '').strip()
        if new_email:
            user.email = new_email
            user.save()
            messages.success(request, "Profile updated.")
            return redirect('profile')
        else:
            messages.error(request, "Please provide a valid email address.")

    return render(request, 'blog/profile.html', {'user_obj': user})


from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from .forms import PostForm

# List all posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

# View single post
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

# Create post
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Update post
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

# Delete post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
