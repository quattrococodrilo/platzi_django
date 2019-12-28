"""Users forms."""

from django import forms


class ProfileForm(forms.Form):
    """Profile form."""
    website = forms.URLField(max_length=200,
                             required=True,
                             widget=forms.URLInput(
                                 attrs={
                                     'class': 'form-control',
                                     'placeholder': 'Website'
                                 }))
    biography = forms.CharField(max_length=500,
                                required=False,
                                widget=forms.Textarea(
                                    attrs={
                                        'class': 'form-control',
                                        'placeholder': 'Biography',
                                        'rows': 3,
                                    }))
    phone_number = forms.CharField(max_length=20,
                                   required=False,
                                   widget=forms.TextInput(attrs={
                                       'class': 'form-control',
                                       'placeholder': 'Phone number'
                                   })
                                   )
    picture = forms.ImageField()
