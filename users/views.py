"""Users views.AssertionError(args)"""

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.shortcuts import redirect, render
from users.models import Profile

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
            return redirect('feed')
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
    return redirect('login')


# ███████ ██ ███    ██  ██████  ██    ██ ██████
# ██      ██ ████   ██ ██       ██    ██ ██   ██
# ███████ ██ ██ ██  ██ ██   ███ ██    ██ ██████
#      ██ ██ ██  ██ ██ ██    ██ ██    ██ ██
# ███████ ██ ██   ████  ██████   ██████  ██

def singup_view(request):
    """Sign up view."""
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        password_confirmation = request.POST.get('password_confirmation', '')
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        email = request.POST.get('email', '')

        if password != password_confirmation:
            return render(request, 'users/signup.html',
                          {'error': 'Password confirmation does not match.'})

        try:
            user = User.objects.create_user(
                username=username, email=email, password=password)
        except IntegrityError:
            return render(request, 'users/signup.html',
                          {'error': 'User name is already in use.'})
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        profile = Profile(user=user)
        profile.save()

        return redirect('login')
    return render(request, 'users/signup.html')

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


def update_profile(request):
    """Update profile."""
    from users.forms import ProfileForm
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
            redirect('update_profile')
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
