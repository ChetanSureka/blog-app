from django.shortcuts import render
from .models import Posts
from django.db.models import Q

def home(request):
    obj = Posts.objects.all()
    context = {
        'posts': obj,
    }
    return render(request, 'api/index.html', context)


def post(request, post_id):
    obj = Posts.objects.get(post_id=post_id)
    context = {
        'post': obj,
    }
    return render(request, 'api/post.html', context)

def search(request):
    query = request.GET.get("q")
    print("Searching...", query)
    filtered_posts = Posts.objects.filter(Q(title__icontains=query) | Q(created_by__username__icontains=query)).order_by('created_at')
    context = {
        'posts': filtered_posts,
        'search': query,
    }
    return render(request, 'api/index.html', context)