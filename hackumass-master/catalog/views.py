from django.shortcuts import render
from catalog.models import Post
from django.views import generic
from django.http import HttpResponseRedirect
from .forms import NameForm


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

def submitPage(request):
    context = {}
    return render(request, 'submit.html', context=context)

def postPage(request):
    context = {}
    #    'posts': Post.objects.all()
    #}
    return render(request, 'posts.html', context = context)


def storage(request):
    context = {}
    return render(request, 'storage.html', context = context)


def Author(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'frontpage.html', {'form': form})

def Title(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'frontpage.html', {'form': form})

def Entry(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'frontpage.html', {'form': form})
