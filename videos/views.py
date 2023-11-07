from django.shortcuts import render, redirect
from django.contrib.auth.decorators import (
    login_required, permission_required)
from .models import Video, Comment
from .forms import VideoForm, CommentsForm


def index(request):
    form = VideoForm()
    videos = Video.objects.all()
    return render(request, 'videos/index.html', {'videos': videos, 'form': form})


def get_video(request, id):
    video = Video.objects.get(id=id)
    comments = Comment.objects.filter(video=id)
    form = CommentsForm()
    return render(request, 'videos/show_video.html', {'video': video, 'comments': comments, 'form': form})


@login_required
@permission_required('videos.add_comment', raise_exception=True)
def add_new_comment(request, id):
    if request.method == 'POST':

        form = CommentsForm(request.POST)

        if form.is_valid():
            user = request.user
            video = Video.objects.get(id=id)
            new_comment = form.save(commit=False)
            new_comment.author = user
            new_comment.video = video

            new_comment.save()

    return redirect('get_video', id)

@login_required
@permission_required('videos.delete_video', raise_exception=True)
def remove_video(request, id):
    video = Video.objects.get(id=id)
    video.delete()
    videos = Video.objects.all()
    return redirect('index')

@login_required
@permission_required('videos.add_video', raise_exception=True)
def add_new_video(request):
    videos = Video.objects.all()
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = VideoForm()
    return render(request, 'videos/index.html', {'videos': videos, 'form': form})
