from django import forms
from django.contrib.auth.models import User




class SignInForm(forms.Form):
    username = forms.CharField(max_length=128)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_password(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        users = User.objects.filter(username=username)
        if len(users) == 0:
            raise forms.ValidationError("Authentification failed")
        user = users[0]
        if not user.check_password(password):
            raise forms.ValidationError("Authentification failed")
        return password


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=128)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean_confirm_password(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('confirm_password')

        if not password2:
            raise forms.ValidationError("You must confirm your password")
        if password1 != password2:
            raise forms.ValidationError("Your passwords do not match")
        return password2

    def  clean_username(self):
        username = self.cleaned_data.get('username')
        users = User.objects.filter(username=username)
        if len(users) > 0:
            raise forms.ValidationError("This username is already taken")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        emails = User.objects.filter(email=email)
        if len(emails) > 0:
            raise forms.ValidationError("This email is already taken")
        return email

class SettingsForm(forms.Form):
    username = forms.CharField(max_length=128, required=False)
    password = forms.CharField(widget=forms.PasswordInput)
    new_password = forms.CharField(widget=forms.PasswordInput, required=False)
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=False)
    userpic = forms.FileField(required=False)






























