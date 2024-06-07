# sticky_notes_project/bulletin_board/tests.py
from django.test import TestCase
from .models import Post


# Create your tests here.
class PostModelTest(TestCase):

    def setUp(self):
        self.post = Post(title="Test Post", content="This is a test post")
        self.post.save()

    def test_post_has_title(self):
        self.assertEqual(self.post.title, "Test Post")

    def test_post_has_content(self):
        self.assertEqual(self.post.content, "This is a test post")

    def test_post_can_be_updated(self):
        self.post.title = "Updated Test Post"
        self.post.content = "This is an updated test post"
        self.post.save()
        self.assertEqual(self.post.title, "Updated Test Post")
        self.assertEqual(self.post.content, "This is an updated test post")

    def test_post_can_be_deleted(self):
        self.post.delete()
        self.assertEqual(Post.objects.all().count(), 0)
