from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, SetPasswordForm, AuthenticationForm, \
    PasswordChangeForm
from django.contrib.auth.models import User
from .models import AccessKey


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'appearance-none block w-full border rounded py-3 '
                        'px-4 leading-tight focus:outline-none',
               'placeholder': '@johndoe'}))

    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'appearance-none block w-full border rounded py-3 px-4 '
                 'leading-tight focus:outline-none',
        'placeholder': 'example@mail.com'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'appearance-none block w-full border rounded py-3 px-4 '
                 'leading-tight focus:outline-none',
        'placeholder': 'Enter your password'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'appearance-none block w-full border rounded py-3 px-4 '
                 'leading-tight focus:outline-none',
        'placeholder': 'Confirm your Password'
    }))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        labels = {
            'username': 'Username',
            'email': 'Email Address',
            'password1': 'Password',
            'password2': 'Confirm Password'
        }
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'appearance-none block w-full border rounded py-3 '
                         'px-4 leading-tight focus:outline-none',
                'placeholder': '@johndoe'
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'appearance-none block w-full border rounded py-3 '
                         'px-4 leading-tight focus:outline-none',
                'placeholder': 'Enter your password'
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'appearance-none block w-full border rounded py-3 '
                         'px-4 leading-tight focus:outline-none',
                'placeholder': 'Confirm your Password'
            }),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'appearance-none block w-full border rounded py-3 px-4 '
                     'leading-tight focus:outline-none',
            'placeholder': '@johndoe'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'appearance-none block w-full border rounded py-3 px-4 '
                     'leading-tight focus:outline-none',
            'placeholder': 'Enter your Password'
        })
    )


class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'appearance-none block w-full border rounded py-3 px-4 '
                 'leading-tight focus:outline-none',
        'placeholder': 'Email'
    }))


class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'appearance-none block w-full border rounded py-3 '
                     'px-4 leading-tight focus:outline-none',
            'placeholder': 'Enter Old Password'
        }),
        label="Old password"
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'appearance-none block w-full border rounded py-3 '
                     'px-4 leading-tight focus:outline-none',
            'placeholder': 'Enter New Password'
        }),
        label="New password"
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'appearance-none block w-full border rounded py-3 '
                     'px-4 leading-tight focus:outline-none',
            'placeholder': 'Confirm New Password'
        }),
        label="Confirm new password"
    )


class CustomSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label="New password",
        widget=forms.PasswordInput(attrs={
            'class': 'appearance-none block w-full border rounded py-3 px-4 '
                     'leading-tight focus:outline-none',
            'placeholder': 'New Password'
        })
    )
    new_password2 = forms.CharField(
        label="Confirm new password",
        widget=forms.PasswordInput(attrs={
            'class': 'appearance-none block w-full border rounded py-3 px-4 '
                     'leading-tight focus:outline-none',
            'placeholder': 'Confirm New Password'
        })
    )


class AccessKeyForm(forms.ModelForm):
    class Meta:
        model = AccessKey
        fields = ['key', 'status', 'expiry_date']
