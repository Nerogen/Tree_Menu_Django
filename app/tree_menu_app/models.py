from django.db import models
from django.db.models import ForeignKey, CharField


class MenuItem(models.Model):
    name: CharField = models.CharField(max_length=100, default="home")
    parent: CharField = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    url: ForeignKey = models.CharField(max_length=255, default="/")
    named_url: CharField = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
