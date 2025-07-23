from django import forms
from .models import URL

class URLForm(forms.Form):
    original_url = forms.URLField(label='Original URL', widget=forms.URLInput(attrs={'class': 'form-control'}))
    custom_code = forms.CharField(
        label='Custom Short Code (optional)',
        max_length=15,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
