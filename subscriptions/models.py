from django.db import models


class Subscribe(models.Model):
    email = models.EmailField(null=False, blank=True, max_length=256, unique=True)
    status = models.CharField(max_length=64, null=False, blank=True)
    created_date = models.DateTimeField(
        "Creation Date", auto_now_add=True, null=False, blank=True
    )
    updated_date = models.DateTimeField(
        "Last Updated Date", auto_now=True, null=False, blank=True
    )

    def __str__(self):
        return self.email
