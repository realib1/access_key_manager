from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash, get_user_model
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode

from .forms import CustomUserCreationForm, CustomPasswordResetForm, AccessKeyForm, CustomAuthenticationForm
from .models import AccessKey
from .email_utils import send_password_reset_email, send_verification_email

User = get_user_model()


def index(request):
    return render(request, "home.html")


# User Signup View
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            send_verification_email(request, user)
            messages.success(request, 'Please confirm your email address to complete the registration')
            return redirect('signin')
        else:
            messages.error(request, 'Invalid credentials, Please try again.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'keymanager/signup.html', {'form': form})


# User Signin View
def signin(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user:
                if not user.email_verified:
                    messages.error(request, 'Email not verified. Kindly check your email inbox to verify!')
                    return redirect('signin')

                login(request, user)
                messages.success(request, '{}, you are now logged in!'.format(user.username))
                return redirect('keylist')
            else:
                messages.error(request, 'Invalid username or password. Please try again!')
                return redirect('signin')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'keymanager/signin.html', {'form': form})


def signout(request):
    logout(request)
    return redirect('index')


@login_required
def change_password(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was changed successfully!')
            return redirect('keylist')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = CustomUserCreationForm(request.user)
    return render(request, 'keymanager/change_password.html', {'form': form})


def password_reset_request(request):
    if request.method == 'POST':
        form = CustomPasswordResetForm(request.POST)
        if form.is_valid():
            user = User.objects.filter(email=form.cleaned_data['email']).first()
            if user:
                send_password_reset_email(request, user)
            messages.success(request, 'Password reset email has been sent.')
            return redirect('signin')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = CustomPasswordResetForm()
    return render(request, 'keymanager/password_reset_form.html', {'form': form})


def password_reset_confirm(request, uidb64=None, token=None):
    return auth_views.PasswordResetConfirmView.as_view(
        template_name='keymanager/password_reset_confirm.html',
        form_class=CustomUserCreationForm,
        success_url=reverse_lazy('password_reset_complete')
    )(request, uidb64=uidb64, token=token)


def password_reset_done(request):
    return render(request, 'keymanager/password_reset_done.html')


def password_reset_complete(request):
    return render(request, 'keymanager/password_reset_complete.html')


@login_required
def create_key(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            access_key = form.save(commit=False)
            access_key.user = request.user
            access_key.save()
            return redirect('keylist')
    else:
        form = AccessKeyForm()
    return render(request, 'home.html', {'form': form})


@login_required
def keylist(request):
    keys = AccessKey.objects.filter(user=request.user)
    return render(request, 'keymanager/keylist.html', {'keys': keys})


@login_required
def keydetails(request, id):
    key = get_object_or_404(AccessKey, id=id)
    return render(request, 'keymanager/keydetails.html', {'key': key})


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = get_user_model().objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Your account has been activated successfully!')
        return redirect('signin')
    else:
        messages.error(request, 'The activation link is invalid or has expired.')
        return redirect('signup')


def resend_verification_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            if not user.is_active:
                send_verification_email(request, user)
                messages.success(request, 'A new verification email has been sent.')
            else:
                messages.info(request, 'This account is already active.')
        except User.DoesNotExist:
            messages.error(request, 'No account found with this email.')
        return redirect('resend_verification')
    return render(request, 'keymanager/resend_verification.html')


def custom_404(request, exception):
    return render(request, '404.html', status=404)
