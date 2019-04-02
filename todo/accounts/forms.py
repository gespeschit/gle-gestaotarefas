from django import forms

from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    """Form definition for User."""

    class Meta:
        """Meta definition for Userform."""

        model = User
        fields = ('first_name','last_name','email','username','password')
