from django import forms
from .models import Book

from cloudinary.forms import CloudinaryFileField



class BookForm(forms.ModelForm):
    image = CloudinaryFileField(options={
        'crop': 'thumb',
        'width': 200,
        'height': 200,
        'folder': 'tagme'
    })
    class Meta:
        model = Book
        fields = ['title', 'description', 'tags', 'image']