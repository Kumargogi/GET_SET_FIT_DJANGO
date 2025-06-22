from django import forms
from .models import CustomUser

class SignupForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['name', 'email', 'password', 'age']
        widgets = {
            'password': forms.PasswordInput(),
        }

class LoginForm(forms.Form):
    name = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
