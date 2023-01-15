from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404,render
from .models import book

class BookListView(generic.ListView):
    model = book
    paginate_by = 6
    template_name = "books/book_list.html"
    context_object_name = 'books'


# class BookDetailView(generic.DetailView):
#     model = book
#     template_name = 'books/book_detail.html'

def book_detail_view(request,pk):
    # get book object
    bok=get_object_or_404(book,pk=pk)
    # get book comments
    book_comments=bok.comments.all()
    return render(request,'books/book_detail.html',{'book':bok,'comments':book_comments})


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
