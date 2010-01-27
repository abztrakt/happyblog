from django.conf.urls.defaults import *
from django.views.generic import date_based, list_detail
from abztrakt.happyblog.models import Post, Tag

object_dict = {
    'queryset': Post.objects.all(),
    'date_field': 'date',
}

tags_dict = {
    'queryset': Tag.objects.all(),
}

urlpatterns = patterns('',
    (r'^tags/(?P<slug>.*)/rss$', 'abztrakt.happyblog.views.tagged_posts_rss', {'posts':Post.objects.all()}),
    (r'^tags/(?P<slug>.*)/', 'abztrakt.happyblog.views.tagged_posts', {'posts':Post.objects.all()}),
    (r'^tags/$', list_detail.object_list, tags_dict),
    (r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/(?P<slug>[0-9A-Za-z-]+)/$', date_based.object_detail, dict(object_dict, slug_field='slug')),
    (r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/$', date_based.archive_day, object_dict),
    (r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$', date_based.archive_month, object_dict),
    (r'^(?P<year>\d{4})/$', date_based.archive_year, dict(object_dict, make_object_list=True)),
    #(r'debug$', 'abztrakt.views.debug', {'debug_in':Post.objects.all()}),
    #(r'^(?P<author>.*)$', 'abztrakt.happyblog.views.author_profile'),
    (r'^(?P<author>.*)/rss$', 'abztrakt.happyblog.views.author_rss', {'posts':Post.objects.all()}),
    (r'^rss$', 'abztrakt.happyblog.views.rss', {'posts':Post.objects.all()}),
    (r'^/?$', date_based.archive_index, object_dict),
)
