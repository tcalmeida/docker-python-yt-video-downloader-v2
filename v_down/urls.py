from django.urls import path
from .views import home_view, fetch_video, process_video

urlpatterns = [
    path('', home_view, name='home'),
    path('description/', fetch_video, name='description'),
    path('download/', process_video, name='download')
]
