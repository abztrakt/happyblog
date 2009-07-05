# Create your views here.

from django.shortcuts import render_to_response

def tagged_posts(request, slug, posts):
    
    posts_tagged = []
    for post in posts:
        for tag in post.assoc_tags.all():
            if slug == tag.slug:
                posts_tagged.append(post)

    return render_to_response('happyblog/tagged_posts.html', locals())
