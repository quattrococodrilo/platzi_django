import json
from datetime import datetime

import requests

import lorem
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
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


@login_required
def list_posts(request):
    """List existing posts."""

    rand_api = 'https://randomuser.me/api'
    resutls = 5
    url_full = '{}?results={}'.format(rand_api, resutls)
    picsum = 'https://picsum.photos/500/700?random={}'
    posts_db = Post.objects.filter(user=request.user).order_by('-created')
    posts = []

    datas_str = requests.get(url_full).text
    datas = json.loads(datas_str).get('results')
    for index, data in enumerate(datas):
        posts.append({
            'title': lorem.sentence(),
            'user': {
                'name': '{} {}'.format(
                    data['name']['first'], data['name']['last']),
                'picture': data['picture']['large'],
            },
            'timestamp': datetime.now(),
            'photo': picsum.format(index + 1)
        })
    for post in posts_db:
        posts.append({
            'title': post.title,
            'user': {
                'name': post.user.get_full_name(),
                'picture': post.profile.picture.url,
            },
            'timestamp': post.created,
            'photo': post.photo.url
        })

    return render(request, 'posts/feed.html', {'posts': posts,
                                               'likes': range(10000)})


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

@login_required
def create_post(request):
    """Create new post view."""
    form = PostForm()
    user = request.user
    profile = user.profile
    if request.method == 'POST':
        data = request.POST.copy()
        data['user'] = user
        data['profile'] = profile
        form = PostForm(data, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('feed')
        else:
            errors = form.errors.as_data()
            title_class = form.fields['title'].widget.attrs
            if 'title' in errors:
                title_class.update({
                    'class': 'form-control is-valid'
                })
            else:
                title_class.update({
                    'class': 'form-control is-valid'
                })
    return render(request,
                  'posts/new.html',
                  {'form': form,
                   'user': user,
                   'profile': profile,
                   })
