from django.shortcuts import render


posts = [
    {
        'author': 'Álvaro Sánchez',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'January 1, 2019',
    },
    {
        'author': 'John Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'January 2, 2019',
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
