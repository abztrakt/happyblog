from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    slug = models.SlugField(max_length=50)

    def get_absolute_url(self):
        return "/blog/tags/%s" % self.slug

    def __unicode__(self):
        return self.slug

class Post(models.Model):
    author = models.ForeignKey(User)
    slug = models.SlugField()
    title = models.CharField(max_length=256)
    date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to="static/uploads/images/%Y/%m/%d", blank=True)
    assoc_tags = models.ManyToManyField(Tag)

    def get_absolute_url(self):
        return "/blog/%s/%s/" % (self.date.strftime("%Y/%b/%d").lower(), self.slug)

    def __unicode__(self):
        return self.slug
