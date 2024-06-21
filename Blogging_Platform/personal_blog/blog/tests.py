from django.test import TestCase,Client
from django.urls import reverse
from .models import Post, Comment, Category

class BlogModelTests(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name="Django")
        self.post = Post.objects.create(title="Test Post", body="Test Body")
        self.post.categories.add(self.category)
        self.comment = Comment.objects.create(
            author="John Doe", body="Test Comment", post=self.post
        )

    def test_category_creation(self):
        self.assertEqual(self.category.name, "Django")

    def test_post_creation(self):
        self.assertEqual(self.post.title, "Test Post")
        self.assertIn(self.category, self.post.categories.all())

    def test_comment_creation(self):
        self.assertEqual(self.comment.author, "John Doe")
        self.assertEqual(self.comment.post, self.post)

class BlogViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(name="Django")
        self.post = Post.objects.create(title="Test Post", body="Test Body")
        self.post.categories.add(self.category)
        self.comment = Comment.objects.create(
            author="John Doe", body="Test Comment", post=self.post
        )

    def test_blog_index_view(self):
        response= self.client.get(reverse('blog_index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post.title)

    def test_blog_category_view(self):
        response = self.client.get(reverse('blog_category', args=[self.category.name]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.category.name)
        self.assertContains(response, self.post.title)

    def test_blog_detail_view(self):
        response = self.client.get(reverse('blog_detail', args=[self.post.pk]))
        self.assertEqual(response.status_code,200)
        self.assertContains(response, self.post.title)
        self.assertContains(response, self.comment.body)