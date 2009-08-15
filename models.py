from django.db import models

class Tag(models.Model):
    slug = models.SlugField(max_length=50)

    def get_absolute_url(self):
        return "/blog/tags/%s" % self.slug

    def __unicode__(self):
        return self.slug

class Post(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=256)
    date = models.DateTimeField()
    body = models.TextField()
    assoc_tags = models.ManyToManyField(Tag)

    def get_absolute_url(self):
        return "/blog/%s/%s/" % (self.date.strftime("%Y/%b/%d").lower(), self.slug)

    def __unicode__(self):
        return self.slug
