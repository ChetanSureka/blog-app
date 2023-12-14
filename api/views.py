from django.shortcuts import render
from .models import Posts

def home(request):
    obj = Posts.objects.last()
    print(obj, obj.content)
    context = {
        'title': obj.title,
        'content': obj.content,
        'created_by': obj.created_by
    }
    return render(request, 'api/index.html', context)

