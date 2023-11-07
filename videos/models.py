from django.utils import timezone
from django.db import models
# Create your models here.

class HashTag(models.Model):
    name = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'
    
class Video(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    video_file = models.FileField(
        upload_to='videos/', null=True, verbose_name="")
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)
    hashtags = models.ManyToManyField(HashTag)

    def __str__(self):
        return f'{self.name}'

 

class Comment(models.Model):
    video = models.ForeignKey(
        Video, to_field='id', on_delete=models.CASCADE
    )
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def update_approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text