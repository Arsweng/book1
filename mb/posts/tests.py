from django.test import TestCase,SimpleTestCase
from .models import Post
from django.urls import reverse
# Create your tests here.
class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text='just a test')
    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name,'just a test')

class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(text = 'this is another test')
    def test_view_status_code_by_link(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    def test_view_status_code_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)
    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))

        self.assertTemplateUsed(resp,'home.html')