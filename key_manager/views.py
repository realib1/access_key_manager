from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm, CustomPasswordResetForm, CustomSetPasswordForm, CustomAuthenticationForm, \
    CustomPasswordChangeForm
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import AccessKey
from .forms import AccessKeyForm
from django.contrib import messages


def index(request):
    return render(request, "home.html")


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, email=email, password=password)
            login(request, user)
            return redirect('singin')
    else:
        form = CustomUserCreationForm()
    return render(request, 'keymanager/signup.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('keylist')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'keymanager/signin.html', {'form': form})


def signout(request):
    logout(request)
    return redirect('index')


def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was changed successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = CustomPasswordChangeForm(request.user)
    return render(request, 'keymanager/change_password.html', {'form': form})


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = CustomPasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            password_reset_form.save(
                request=request,
                use_https=request.is_secure(),
                email_template_name='keymanager/password_reset_form.html'
            )
            return redirect('password_reset_done')
    else:
        password_reset_form = CustomPasswordResetForm()
    return render(request, 'keymanager/password_reset_form.html', {'form': password_reset_form})


def password_reset_done(request):
    return render(request, 'keymanager/password_reset_done.html')


def password_reset_confirm(request, uidb64=None, token=None):
    return auth_views.PasswordResetConfirmView.as_view(
        template_name='keymanager/password_reset_confirm.html',
        form_class=CustomSetPasswordForm,
        success_url=reverse_lazy('password_reset_complete')
    )(request, uidb64=uidb64, token=token)


def password_reset_complete(request):
    return render(request, 'keymanager/password_reset_complete.html')


@login_required
def create_key(request):
    if request.method == 'POST':
        form = AccessKeyForm(request.POST)
        if form.is_valid():
            access_key = form.save(commit=False)
            access_key.user = request.user
            access_key.save()
            return redirect('keylist')
    # else:
    #     form = AccessKeyForm()
    # return render(request, 'keymanager/create_key.html', {'form': form})


@login_required
def keylist(request):
    keys = AccessKey.objects.filter(user=request.user)
    return render(request, 'keymanager/keylist.html', {'keys': keys})


@login_required
def keydetails(request, id):
    key = get_object_or_404(AccessKey, id=id)
    return render(request, 'keymanager/keydetails.html', {'key': key})


def custom_404(request, exception):
    return render(request, '404.html', status=404)
