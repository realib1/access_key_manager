import threading

from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.conf import settings
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator


class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()


def send_verification_email(request, user):
    current_site = get_current_site(request)
    domain = current_site.domain
    port = '8000'
    domain = f"{domain}:{port}"
    subject = 'Activate your account.'
    email_message = render_to_string('keymanager/account_activation_email.html', {
        'user': user,
        'domain': domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': default_token_generator.make_token(user),
    })

    send_mail(subject, email_message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)


def send_password_reset_email(user, token):
    subject = 'Password Reset Request'
    email_message = render_to_string('keymanager/password_reset_form.html', {'user': user, 'token': token})

    send_mail(subject, email_message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)
