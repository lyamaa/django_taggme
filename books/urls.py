
from django.urls import path

from .views import home, create

app_name = 'books'

urlpatterns = [
  path('', home, name='home'),
  path('tag/<str:pk>', home, name="books_tag"),
  path('create', create, name="create" )
]
