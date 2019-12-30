"""Users views.AssertionError(args)"""

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, UpdateView
from posts.models import Post
from users.forms import SignupForm
from users.models import Profile, User

# ██       ██████   ██████  ██ ███    ██
# ██      ██    ██ ██       ██ ████   ██
# ██      ██    ██ ██   ███ ██ ██ ██  ██
# ██      ██    ██ ██    ██ ██ ██  ██ ██
# ███████  ██████   ██████  ██ ██   ████


class LoginView(auth_views.LoginView):
    """Login view."""
    template_name = 'users/login.html'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['username'].widget.attrs.update({
            'class': 'form-control'})
        form.fields['password'].widget.attrs.update({
            'class': 'form-control'})
        return form

    def get(self, request, *args, **kwargs):
        """Handle GET requests: instantiate a blank version of the form."""
        if request.user.is_authenticated:
            return redirect('posts:feed')
        return super().get(request, args, kwargs)


# ██       ██████   ██████   ██████  ██    ██ ████████
# ██      ██    ██ ██       ██    ██ ██    ██    ██
# ██      ██    ██ ██   ███ ██    ██ ██    ██    ██
# ██      ██    ██ ██    ██ ██    ██ ██    ██    ██
# ███████  ██████   ██████   ██████   ██████     ██

class LogoutView(auth_views.LogoutView):
    """Logout a user."""
    next_page = reverse_lazy('users:login')


# ███████ ██ ███    ██  ██████  ██    ██ ██████
# ██      ██ ████   ██ ██       ██    ██ ██   ██
# ███████ ██ ██ ██  ██ ██   ███ ██    ██ ██████
#      ██ ██ ██  ██ ██ ██    ██ ██    ██ ██
# ███████ ██ ██   ████  ██████   ██████  ██

class SignupView(FormView):
    """Sign up view."""
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """Save form data."""
        form.save()
        return super().form_valid(form)

# ██    ██ ██████  ██████   █████  ████████ ███████
# ██    ██ ██   ██ ██   ██ ██   ██    ██    ██
# ██    ██ ██████  ██   ██ ███████    ██    █████
# ██    ██ ██      ██   ██ ██   ██    ██    ██
#  ██████  ██      ██████  ██   ██    ██    ███████

# ██████  ██████   ██████  ███████ ██ ██      ███████
# ██   ██ ██   ██ ██    ██ ██      ██ ██      ██
# ██████  ██████  ██    ██ █████   ██ ██      █████
# ██      ██   ██ ██    ██ ██      ██ ██      ██
# ██      ██   ██  ██████  ██      ██ ███████ ███████


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """Update profile."""
    template_name = 'users/update_profile.html'
    model = Profile
    fields = ['website', 'biography', 'phone_number', 'picture']

    def get_object(self):
        """Return user's profile."""
        return self.request.user.profile

    def get_success_url(self):
        """Return to user's profile"""
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username': username})

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['website'].widget.attrs.update({
            'class': 'form-control'})
        form.fields['biography'].widget.attrs.update({
            'class': 'form-control',
            'rows': 3})
        form.fields['phone_number'].widget.attrs.update({
            'class': 'form-control'})
        return form


# ██████  ███████ ████████  █████  ██ ██
# ██   ██ ██         ██    ██   ██ ██ ██
# ██   ██ █████      ██    ███████ ██ ██
# ██   ██ ██         ██    ██   ██ ██ ██
# ██████  ███████    ██    ██   ██ ██ ███████

# ██    ██ ██ ███████ ██     ██
# ██    ██ ██ ██      ██     ██
# ██    ██ ██ █████   ██  █  ██
#  ██  ██  ██ ██      ██ ███ ██
#   ████   ██ ███████  ███ ███


class DetailView(LoginRequiredMixin, DetailView):
    """Detail user data"""
    template_name = 'users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    context_object_name = 'user'
    model = User
    queryset = User.objects.all()

    def get_context_data(self, **kwargs):
        """Add user's posts to context"""
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context
