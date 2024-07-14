from django.urls import path

from books.views import book_create, book_details, BookEditView, book_borrow, BookDeleteView, my_books, \
    my_borrowed_books, borrowed_books, book_returned

urlpatterns = [
    path('add', book_create, name='add book'),
    path('details/<int:pk>/', book_details, name='book details'),
    path('edit/<int:pk>/', BookEditView.as_view(), name='book edit'),
    path('borrow/<int:pk>/', book_borrow, name='book borrow'),
    path('delete/<int:pk>/', BookDeleteView.as_view(), name='book delete'),
    path('my-books/<int:pk>/', my_books, name='my books'),
    path('my-borrowed-books/<int:pk>/', my_borrowed_books, name='my borrowed books'),
    path('borrowed-books/<int:pk>', borrowed_books, name='borrowed books'),
    path('book-returned/<int:pk>', book_returned, name='book returned'),
]
