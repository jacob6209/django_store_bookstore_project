from django.views import generic

from .models import book

class BookListView(generic.ListView ):
    model = book
    template_name = "books/book_list.html"
    context_object_name = 'books'


