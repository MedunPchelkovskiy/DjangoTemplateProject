from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField, AuthenticationForm
from django.contrib.auth import get_user_model
from django.forms import ValidationError

from accounts_manage.models import UserProfile

UserModel = get_user_model()


class SignUpForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = (UserModel.USERNAME_FIELD,)
        field_classes = {'username': UsernameField}

    def save(self, commit=True):  # create user with empty profile
        user = super().save(
            commit=commit)  # if create not empty profile with registration, add and profile info fields(first_name=self.cleaned_data['first_name'], last_name=self.cleaned_data['last_name']....)
        profile = UserProfile(
            user=user, )  # can add here first_name = first_name. lasT_name = last_name ...  or **self.cleaned_data
        if commit:
            profile.save()

        return user


class SignInForm(AuthenticationForm):
    username = UsernameField(
        label=('Username'),
        widget=forms.TextInput(
            attrs={'autofocus': True,
                   'placeholder': 'Username'})
    )

    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'current-password',
                   'placeholder': 'Password'})
    )


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['email', 'first_name', 'last_name', 'age',]
        labels = {
            'email': 'Email',
            'first_name': 'First Name:',
            'last_name': 'Last Name:',
            'age': 'Age:'
        }

        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'age': forms.NumberInput(attrs={'placeholder': 'Age'})
        }

    # fields = ('username', 'password')
    # # username = UsernameField()
    # # password = forms.TextInput()

    # labels = {
    #     'username': 'Username',
    #     'password': 'Password'
    # }

    # widgets = {
    #     'username': forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Username'}),
    #     'password': forms.PasswordInput(attrs={'autocomplete': 'current-password', 'placeholder': 'Password'})
    # }