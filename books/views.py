from django.views import generic
from django.urls import reverse_lazy

from .models import book

class BookListView(generic.ListView):
    model = book
    paginate_by = 6
    template_name = "books/book_list.html"
    context_object_name = 'books'


class BookDetailView(generic.DetailView):
    model = book
    template_name = 'books/book_detail.html'

class BookCreateView(generic.CreateView):
    model = book
    fields = ['title','author','description','price','cover']
    template_name = 'books/book_create.html'

class BookUpdateView(generic.UpdateView):
    model = book
    fields = ['title', 'author', 'description','price','cover']
    template_name = 'books/book_update.html'

class BookDeleteView(generic.DeleteView):
    model = book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy("book_list")
