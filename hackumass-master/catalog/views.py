from django.shortcuts import render
from catalog.models import Post
from django.views import generic

posts = [
    {
        'author': 'Jane Doe',
            'title': 'Blog Post 2',
            'content': 'Second post content',
            'date_posted': 'August 28, 2018',
    },
    { 'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018',
        },
]

# Create your views here.


def frontpage(request):
    #View function for home page of site."""
    context = {
        'posts': posts
        #'posts' assigned to post key
        #keyname will be accesible (data)
        #'posts' variable available

    }
    return render(request, 'frontpage.html', context= context )
def postPage(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'posts.html', context = context)
