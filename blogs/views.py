from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from blogs.models import Blog, Category

# Create your views here.
def posts_by_category(request, category_id):
    # Fetch the posts that belong to the category with the id category_id
    posts = Blog.objects.filter(status='published', category=category_id)
    
    # # Use try/except when we want to do some cunstome actions
    # try:
    #     category = Category.objects.get(pk=category_id)
    # except:
    #     return redirect('home')
    
    # Use get_object_or_404 when you want to show 404 error ppage if category does not exist
    category = get_object_or_404(Category, pk=category_id)
        
    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'posts_by_category.html', context)