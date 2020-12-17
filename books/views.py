from django.shortcuts import get_object_or_404, render, redirect

from taggit.models import Tag
from books.models import Book

from .forms import BookForm


def home(request, pk=None):
    tag_obj = None

    if not pk:
        books = Book.objects.all()
    else:
        tag_obj = get_object_or_404(Tag, pk=pk)
        books = Book.objects.filter(tags__in=[tag_obj])

    return render(request, 'home.html', {
        'tag': tag_obj,
        'books': books
    })


def create(request, *args, **kwargs):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.author = request.user
            form.save()
            return redirect('books:home')
    else:
        form = BookForm()
        return render(request, 'create.html', {
            "form": form
        })
