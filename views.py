from django.shortcuts import render_to_response
from abztrakt.happyblog.models import User

def author_profile(request, author):
    return render_to_response('profile.html', locals())

def author_rss(request, author, posts):
    """ Parses posts for a particular author to the RSS template. lastdate is the publish date of the most recent post for that author.
    """
    posts = posts.order_by('date').reverse()

    posts_author = []
    for post in posts:
        if post.author.username == author:
            posts_author.append(post)

    posts = posts_author
    lastdate = posts_author[0].date

    return render_to_response('rss.xml', locals())


def tagged_posts(request, slug, posts):
    """ Returns posts for a particular tag. The slug is the tag.
    """
    posts_tagged = []
    for post in posts:
        for tag in post.assoc_tags.all():
            if slug == tag.slug:
                posts_tagged.append(post)

    return render_to_response('tagged_posts.html', locals())


def tagged_posts_rss(request, slug, posts):
    """ Passes posts for a particular tag to the RSS template. lastdate is the publish date of the most recent post for that tag.
    """
    posts = posts.order_by('date').reverse()

    posts_tagged = []
    for post in posts:
        for tag in post.assoc_tags.all():
            if slug == tag.slug:
                posts_tagged.append(post)

    posts = posts_tagged
    lastdate = posts_tagged[0].date

    return render_to_response('rss.xml', locals())


def rss(request, posts):
    """ Passes all posts into the RSS template. lastdate is the publish date of the most recent post.
    """
    posts = posts.order_by('date').reverse()
    lastdate = posts[0].date
    return render_to_response('rss.xml', locals())
