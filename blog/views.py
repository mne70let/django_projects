from django.shortcuts import render
from django.utils import timezone
from .models import Post #import model. Dot means same folder/app

def post_list(request):
    posts = Post.objects.order_by('published_date')
    # render with additional model derived input for template
    return render(request, 'blog/post_list.html', {'posts': posts})