from django.contrib.auth.models import User, AbstractUser,  Group, Permission
from django.db import models
from key_manager.utils import generate_key


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, default='default@example.com')
    groups = models.ManyToManyField(Group, related_name='customuser_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set', blank=True)


# Create your models here.
class AccessKey(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    key = models.CharField(max_length=25, unique=True, default=generate_key)
    status = models.CharField(max_length=50,
                              choices=[('active', 'Active'), ('Expired', 'Expired'), ('revoked', 'Revoked')])
    procurement_date = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateTimeField()
    usage_count = models.IntegerField(default=0)
    max_usage = models.IntegerField(default=1)
    metadata = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.email} - {self.key}"

