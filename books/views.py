from django.shortcuts import render
from .models import Book
from django.views.generic import ListView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q


class BookListView(ListView):
    template_name = 'books/book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        query = self.request.GET.get('search', 0)
        if query:
            return Book.objects.filter(
                Q(title__icontains=query) |
                Q(author=query)
            )
        return Book.objects.all()


class BookDetailView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        book = Book.objects.get(id=self.kwargs['pk'])
        reviews = book.reviews.all()
        return render(request, 'books/book_detail.html', context={'book': book, 'reviews': reviews})
