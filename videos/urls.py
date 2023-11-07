from django.contrib import admin
from django.urls import path
from .views import index, get_video, add_new_comment, remove_video, add_new_video

urlpatterns = [
    path('', index, name='index'),
    path('video/<int:id>',get_video, name='get_video'),   
    path('video/<int:id>/add_new_comment',
         add_new_comment,
         name='add_new_comment'),
    path('video/add_new_video',
         add_new_video,
         name='add_new_video'),
    path('video/<int:id>/remove_video',
         remove_video,
         name='remove_video')
]