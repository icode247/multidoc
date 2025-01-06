from django.db import models
from django.contrib.auth.models import User
from core.models import Organization

class Document(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
