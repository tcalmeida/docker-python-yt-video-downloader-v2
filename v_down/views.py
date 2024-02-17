from django.shortcuts import render, redirect
from django.http import FileResponse
from pathlib import Path
from pytube import YouTube
from pytube.exceptions import RegexMatchError

BASE_DIR = Path(__file__).resolve().parent.parent
downloaded_video_path = BASE_DIR / 'video_files'


def home_view(request):
    return render(request, 'index.html')


def fetch_video(request):
    try:
        if request.POST.get('fetch_url'):
            link = request.POST.get('url_video')
            yt_video = YouTube(link)
            title = yt_video.title
            thumb_video = yt_video.thumbnail_url
            file_size = round(yt_video.streams.get_highest_resolution().filesize_mb)

            context = {'title': title, 'thumb_video': thumb_video, 'file_size': file_size, 'link': link}
            return render(request, 'description.html', context)
        return render(request, 'description.html')
    except RegexMatchError:
        return render(request, 'error.html')

def process_video(request):
    if request.POST.get('download_video'):
        url = request.POST.get('url')
        yt_video = YouTube(url)
        title = yt_video.title
        download_file = yt_video.streams.get_highest_resolution()
        return FileResponse(open(download_file.download(output_path=str(downloaded_video_path)), 'rb'),
                            as_attachment=True, filename=f'{title}.mp4')
    return redirect('home')
