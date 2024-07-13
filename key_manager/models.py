from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class AccessKey(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    key = models.CharField(max_length=50, unique=True)
    status = models.CharField(max_length=50, choices=[('active', 'Active'), ('expired', 'Expired'), ('revoked', 'Revoked')])
    procurement_date = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateTimeField()
    usage_count = models.IntegerField(default=0)
    max_usage = models.IntegerField(default=1)
    metadata = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.email} - {self.key}"

