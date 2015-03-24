from django.db import models
import uuid


class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    description = models.CharField(blank=True, max_length=100)
    complete = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)
