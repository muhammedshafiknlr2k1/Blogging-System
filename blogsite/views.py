from django.shortcuts import render
from blogs.models import Category, Blogs

def home(request):
    categories = Category.objects.all()
    featured_posts = Blogs.objects.filter(is_featured=True).order_by('-updated_at')
    context = {
        'categories' : categories,
        'featured_posts' : featured_posts
    }
    return render(request, 'home.html', context)