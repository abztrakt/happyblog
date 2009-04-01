from django.db import models

class Post(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=256)
    date = models.DateTimeField()
    body = models.TextField()

    def __unicode__(self):
        return self.slug
