"""Post forms."""
from django import forms
from posts.models import Post


class PostForm(forms.ModelForm):
    """Post model forms."""

    class Meta:
        model = Post
        fields = ('user', 'profile', 'title', 'photo')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title',
            }),
        }
