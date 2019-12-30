"""Users views.AssertionError(args)"""

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.generic.detail import DetailView
from users.forms import ProfileForm, SignupForm
from users.models import User

# ██       ██████   ██████  ██ ███    ██
# ██      ██    ██ ██       ██ ████   ██
# ██      ██    ██ ██   ███ ██ ██ ██  ██
# ██      ██    ██ ██    ██ ██ ██  ██ ██
# ███████  ██████   ██████  ██ ██   ████


def login_view(request):
    """Login view."""
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('posts:feed')
        else:
            return render(request, 'users/login.html',
                          {'error': 'Invalid username and password'})

    return render(request, 'users/login.html')


# ██       ██████   ██████   ██████  ██    ██ ████████
# ██      ██    ██ ██       ██    ██ ██    ██    ██
# ██      ██    ██ ██   ███ ██    ██ ██    ██    ██
# ██      ██    ██ ██    ██ ██    ██ ██    ██    ██
# ███████  ██████   ██████   ██████   ██████     ██

@login_required
def logout_view(request):
    """Logout a user."""
    logout(request)
    return redirect('users:login')


# ███████ ██ ███    ██  ██████  ██    ██ ██████
# ██      ██ ████   ██ ██       ██    ██ ██   ██
# ███████ ██ ██ ██  ██ ██   ███ ██    ██ ██████
#      ██ ██ ██  ██ ██ ██    ██ ██    ██ ██
# ███████ ██ ██   ████  ██████   ██████  ██

def singup_view(request):
    """Sign up view."""
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    return render(request,
                  'users/signup.html',
                  {'form': form})

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


@login_required
def update_profile(request):
    """Update profile."""
    form = ProfileForm()
    user = request.user
    profile = user.profile

    form.fields['website'].initial = profile.website
    form.fields['biography'].initial = profile.biography
    form.fields['phone_number'].initial = profile.phone_number
    form.fields['picture'].initial = profile.picture

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)

        if form.is_valid():
            data = form.cleaned_data
            profile.website = data.get('website', '')
            profile.biography = data.get('biography', '')
            profile.phone_number = data.get('phone_number', '')
            profile.picture = data.get('picture', '')
            profile.save()
            redirect('posts:feed')
        else:
            errors = form.errors.as_data()
            if 'website' in errors:
                form.fields['website'].widget.attrs.update(
                    {'class': 'form-control is-invalid'})

    return render(request,
                  'users/update_profile.html',
                  {'user': user,
                   'profile': profile,
                   'form': form, })


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


class DetailView(DetailView):
    """Detail user data"""
    template_name = 'users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    model = User

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['now'] = timezone.now()
    #     return context
