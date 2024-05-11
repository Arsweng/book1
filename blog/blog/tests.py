import email
from email.quoprimime import body_check
from turtle import title
from urllib import response
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Post
# Create your tests here.

class BlogTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email = 'test@test.com',
            password = 'test123'
        )
        self.post = Post.objects.create(
            title = 'this is the title',
            body = 'this is a body',
            author = self.user
        )

    def test_string_representaion(self):
        post = Post(title = 'a simple title')

        self.assertEqual(str(post),post.title)
    
    def test_post_content(self):
        self.assertEqual(f'{self.post.title}','this is the title')
        self.assertEqual(f'{self.post.author}','testuser')
        self.assertEqual(f'{self.post.body}','this is a body')
    
    def test_post_list_view(self):
        resp = self.client.get(reverse('home'))
        self.assertContains(resp, 'this is the title')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp,'home.html')
    
    def test_post_details_view(self):
        resp = self.client.get('/post/1')
        non_resp = self.client.get('/post/999999999999')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(non_resp.status_code, 404)
        self.assertTemplateUsed(resp, 'post_details.html')
        self.assertContains(resp,'this is a body')

    def test_create_post_view(self):
        response = self.client.post(reverse('post_new'),{
            'title':'new title',
            'body':'new body',
            'author':self.user
        })
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'new title')
    
    def test_update_post_view(self):
        response = self.client.post(reverse('post_edit', args='1'),{
            'title':'updated title',
            'body':'updated body',
        })

        self.assertEqual(response.status_code, 302)

    def test_delete_post_view(self):
        response = self.client.get(
        reverse('post_delete', args='1'))
        self.assertEqual(response.status_code, 200)