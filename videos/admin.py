from django.contrib import admin
from .models import Video, HashTag, Comment

# Register your models here.
admin.site.register(Video)
admin.site.register(HashTag)
admin.site.register(Comment)