from django.views import generic

from .models import book

class BookListView(generic.ListView):
    model = book
    template_name = "books/book_list.html"
    context_object_name = 'books'


class BookDetailView(generic.DetailView):
    model = book
    template_name = 'books/book_detail.html'

class BookCreateView(generic.CreateView):
    model = book
    fields = ['title','author','description','price']
    template_name = 'books/book_create.html'
class BookUpdateView(generic.UpdateView):
    model = book
    fields = ['title', 'author', 'description','price']
    template_name = 'books/book_update.html'



