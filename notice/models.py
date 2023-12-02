from django.db import models
from django.contrib.auth.models import User
import os

class NoticePost(models.Model):
    title = models.CharField(max_length=30, blank=True)

    content = models.TextField()

    notice_image = models.ImageField(upload_to='notice/images/%Y/%m/%d/', blank=True)
    top_fixed = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)


    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    view_count = models.IntegerField(default=0)

    def __str__(self):
        return f'[{self.pk}]{self.title} :: {self.author}'

    def get_absolute_url(self):
        return f'/notice/{self.pk}/'
