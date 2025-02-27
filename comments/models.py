from django.db import models

# Create your models here.
class Comment(models.Model):
    username = models.CharField(max_length=30)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.username} - {self.comment[:40]}...'