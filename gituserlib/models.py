from django.db import models


class User(models.Model):
    date_joined = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=255,null=True)
    username = models.CharField(max_length=255,unique=True)
    is_active = models.BooleanField(default=True)
    class Meta:
        app_label = 'gituserlib'
        managed = True