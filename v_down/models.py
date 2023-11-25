from django.db import models


class Link(models.Model):
    video_link = models.CharField(max_length=200)

    def __str__(self):
        return self.video_link
