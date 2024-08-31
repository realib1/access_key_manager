from django.conf import settings
from django.utils import timezone
from dateutil.relativedelta import relativedelta
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from key_manager.utils import generate_key


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    email_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    groups = models.ManyToManyField(Group, related_name='customuser_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set', blank=True)


class AccessKey(models.Model):
    school_name = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    key = models.CharField(max_length=25, unique=True, default=generate_key)
    status = models.CharField(max_length=50,
                              choices=[('active', 'Active'), ('Expired', 'Expired'), ('revoked', 'Revoked')])
    procurement_date = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateTimeField()
    usage_count = models.IntegerField(default=0)
    max_usage = models.IntegerField(default=1)
    metadata = models.JSONField(null=True, blank=True)
    #
    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         self.expiry_date = timezone.now() + relativedelta(months=1)
    #     super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.email} - {self.key}"
