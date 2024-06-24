from django.test import TestCase, RequestFactory
from rest_framework.test import APIRequestFactory, force_authenticate, APITestCase, APIClient
from rest_framework import status
from .models import Book
from .serializers import BookSerializer
from .views import BookCreateListView
from django.urls import reverse


#using  ' RequestFactory '

class BookAPITestCaseRF(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.book1 = Book.objects.create(
            title='Book 1',
            author='Author 1',
            published_date='2024-04-23'
        )
        self.book2 = Book.objects.create(
            title='Book 2',
            author='Author 2',
            published_date='2024-06-18'
        )
        self.book_list_url = reverse('book_listclass')

    def test_get_book_list(self):
        request = self.factory.get(self.book_list_url)
        view = BookCreateListView.as_view()
        response = view(request)
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_book(self):
        data = {
            'title': 'test Book',
            'author': 'book author',
            'published_date': '2022-02-02'
        }
        request = self.factory.post(self.book_list_url, data, format='json')
        view = BookCreateListView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.get(id=3).title, 'test Book')

    def test_create_book_invalid_data(self):
        data = {
            'title':'',
            'author':'New Author',
            'published_date': '2024-06-19'
        }
        request = self.factory.post(self.book_list_url, data, format='json')
        view = BookCreateListView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


#using  ' APIRequestFactory '

class BookAPITestCase_APIRF(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.book1 = Book.objects.create(
            title='Book 1',
            author='Author 1',
            published_date='2024-04-23'
        )
        self.book2 = Book.objects.create(
            title='Book 2',
            author='Author 2',
            published_date='2024-06-18'
        )
        self.book_list_url = reverse('book_listclass')

    def test_get_book_list(self):
        request = self.factory.get(self.book_list_url)
        view = BookCreateListView.as_view()
        response = view(request)
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_book(self):
        data = {
            'title': 'test Book',
            'author': 'book author',
            'published_date': '2022-02-02'
        }
        request = self.factory.post(self.book_list_url, data, format='json')
        view = BookCreateListView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.get(id=3).title, 'test Book')

    def test_create_book_invalid_data(self):
        data = {
            'title':'',
            'author':'New Author',
            'published_date': '2024-06-19'
        }
        request = self.factory.post(self.book_list_url, data, format='json')
        view = BookCreateListView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


# API Client testing

class BookAPITestCase_APIClient(TestCase):
    def setUp(self):
        self.client =  APIClient()
        self.book1 = Book.objects.create(
            title ='Book 1',
            author = 'Author 1',
            published_date = '2024-04-17'
        )
        self.book2 = Book.objects.create(
            title='Book 2',
            author='Author 2',
            published_date='2024-06-18'
        )
        self.book_list_url = reverse('book_listclass')

    def test_get_book_list(self):
        response = self.client.get(self.book_list_url)
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_book(self):
        data = {
            'title': 'test Book',
            'author': 'Author_Book',
            'published_date':'2024-06-19'
        }
        response = self.client.post(self.book_list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.get(id=3).title, 'test Book')

    def test_create_book_invalid_data(self):
        data = {
            'title': '',
            'author': 'New Author',
            'published_date': '2024-05-23'
        }
        response = self.client.post(self.book_list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)