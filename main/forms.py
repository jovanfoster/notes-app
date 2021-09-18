from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError('A user has already registered using this username')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('A user has already registered using this email')
        return email

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.username = self.clean_username()
        user.email = self.clean_email()
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
