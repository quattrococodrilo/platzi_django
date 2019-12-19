from django.shortcuts import render


def list_posts(request):
    """List existing posts."""
    return render(request, 'feed.html')
