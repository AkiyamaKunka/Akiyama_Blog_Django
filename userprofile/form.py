from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

class UserRegisterForm(forms.ModelForm):
    # rewrite user's password
    password = forms.CharField()
    password_2 = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'email')

    # check if passwords are the same
    def clean_password_2(self):
        data = self.cleaned_data
        if data.get('password') == data.get('password_2'):
            return data.get('password')
        else:
            raise forms.ValidationError("Password inconsistent, please try again.")

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone', 'avatar', 'bio')


