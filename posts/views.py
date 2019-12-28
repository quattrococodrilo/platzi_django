from django.contrib.auth.decorators import login_required
from django.shortcuts import render, reverse


@login_required
def list_posts(request):
    """List existing posts."""

    import json
    import requests
    import lorem
    from datetime import datetime

    rand_api = 'https://randomuser.me/api'
    resutls = 5
    url_full = '{}?results={}'.format(rand_api, resutls)
    picsum = 'https://picsum.photos/500/700?random={}'

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

    return render(request, 'posts/feed.html', {'posts': posts})
