from django.shortcuts import get_object_or_404, render

from taggit.models import Tag
from books.models import Book

def home(request, pk=None):
    tag_obj = None

    if not pk:
        books = Book.objects.all()
    else:
        tag_obj = get_object_or_404(Tag, pk=pk)
        books = Book.objects.filter(tag__in=[tag_obj])
    
    return render(request, 'home.html',{
        'tag': tag_obj,
        'books': books
    })
