# sticky_notes_app/models.py
from django.db import models


# Create your models here.
# Note class contains title, content, when it was created and updated.
class Note(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
