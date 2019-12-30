from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from posts.forms import PostForm
from posts.models import Post

# ██      ██ ███████ ████████
# ██      ██ ██         ██
# ██      ██ ███████    ██
# ██      ██      ██    ██
# ███████ ██ ███████    ██

# ██████   ██████  ███████ ████████ ███████
# ██   ██ ██    ██ ██         ██    ██
# ██████  ██    ██ ███████    ██    ███████
# ██      ██    ██      ██    ██         ██
# ██       ██████  ███████    ██    ███████


class PostsFeedView(LoginRequiredMixin, ListView):
    """Return all published posts"""
    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created',)
    paginate_by = 30
    context_object_name = 'posts'


# ███    ██ ███████ ██     ██
# ████   ██ ██      ██     ██
# ██ ██  ██ █████   ██  █  ██
# ██  ██ ██ ██      ██ ███ ██
# ██   ████ ███████  ███ ███

# ██████   ██████  ███████ ████████
# ██   ██ ██    ██ ██         ██
# ██████  ██    ██ ███████    ██
# ██      ██    ██      ██    ██
# ██       ██████  ███████    ██

class CreatePostView(LoginRequiredMixin, CreateView):
    """Create a new post."""
    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')

    def get_form(self, form_class=None):
        """Return an instance of the form to be used in this view."""
        kwargs = self.get_form_kwargs()

        post = self.request.POST.copy()
        post['user'] = self.request.user
        post['profile'] = self.request.user.profile

        kwargs.update({'data': post})

        if form_class is None:
            form_class = self.get_form_class()
        return form_class(**kwargs)

# ██████  ███████ ████████  █████  ██ ██
# ██   ██ ██         ██    ██   ██ ██ ██
# ██   ██ █████      ██    ███████ ██ ██
# ██   ██ ██         ██    ██   ██ ██ ██
# ██████  ███████    ██    ██   ██ ██ ███████

# ██████   ██████  ███████ ████████
# ██   ██ ██    ██ ██         ██
# ██████  ██    ██ ███████    ██
# ██      ██    ██      ██    ██
# ██       ██████  ███████    ██


class PostDetail(LoginRequiredMixin, DetailView):
    template_name = 'posts/detail.html'
    model = Post
    context_object_name = 'post'
