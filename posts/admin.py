# Django
from django.contrib import admin
# Models
from posts.models import Post

# ██████   ██████  ███████ ████████
# ██   ██ ██    ██ ██         ██
# ██████  ██    ██ ███████    ██
# ██      ██    ██      ██    ██
# ██       ██████  ███████    ██


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created')
