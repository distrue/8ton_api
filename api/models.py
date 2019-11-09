from django.db import models
from jsonfield import JSONField


class Post(models.Model):
    # id: auto generated
    author = models.CharField(max_length=50)
    meta = JSONField(default={}, dump_kwargs={'ensure_ascii': False})
    keywords = JSONField(default={}, dump_kwargs={'ensure_ascii': False})
    posts = JSONField(default={}, dump_kwargs={'ensure_ascii': False})
