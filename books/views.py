from django.core.paginator import Paginator
from django.shortcuts import render

from books.models import Book


def books_view(request):
    books = Book.objects.all()
    book_list = list()
    for book in books:
        book_dict = {}
        book_dict['name'] = book.name
        book_dict['author'] = book.author
        book_dict['pub_date'] = book.pub_date.strftime('%Y-%m-%d')
        book_list.append(book_dict)

    page_book = request.GET.get('pub_date', '')
    print(page_book)
    paginator = Paginator(book_list, 1)
    template = 'books/?{page_book}.html'
    page = paginator.get_page(page_book)
    print(page)

    template = 'books/books_list.html'
    if page_book:
        print('Da')
        for book in book_list:
            if page_book in book.values():
                page = paginator.get_page(page_book)
        context = {
            'page': page
        }
    elif not page_book:
        print('NET')
        context = {
            'books': book_list
        }
    return render(request, template, context)
