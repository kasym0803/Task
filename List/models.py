from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    completed = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
