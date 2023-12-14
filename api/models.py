from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
import uuid

class Posts(models.Model):
    post_id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4())
    title = models.CharField(max_length=300)
    content = RichTextField()
    created_by = models.ForeignKey(User, related_name="posts", on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
