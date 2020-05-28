from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class BookmarkSaveForm(forms.Form):
    url = forms.URLField(
        label='address',
        widget=forms.TextInput(attrs={'size': 64})
    )

    title = forms.CharField(
        label='title',
        widget=forms.TextInput(attrs={'size': 64})
    )

    tags = forms.CharField(
        label='tag',
        required=False,
        widget=forms.TextInput(attrs={'size': 64})
    )