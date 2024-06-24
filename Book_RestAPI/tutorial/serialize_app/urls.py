from django.urls import path
from .views import BookListCreateView, BookDetailView, BookListView, BookCreateListView, books_list
from . import views

urlpatterns = [
    path('', BookListCreateView.as_view(), name='book-list-create'),
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('api/books_fun/', views.book_list, name='book_list'),
    path('api/books_class/', BookListView.as_view(), name='book_listcl'),
    path('books_list/', books_list, name='books_list'),
    path('book_listclass/', BookCreateListView.as_view(), name='book_listclass'),
    path('booksbrow/', BookCreateListView.as_view(), name='book-list-create'),

]
