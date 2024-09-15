from django.shortcuts import render
from django.http import FileResponse
from .utils.utils import create_video

def index(request):
    message = str(request.GET.get("message", ""))

    create_video(message)
    video = open(f"runtext/utils/video/{message}.mp4", "rb")

    return FileResponse(video, content_type="video/mp4v")
