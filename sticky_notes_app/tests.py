from django.test import TestCase
from .models import Note


# Create your tests here.
class NoteModelTest(TestCase):
    def setUp(self):
        self.note = Note(title="Test Note", content="This is a test note")
        self.note.save()

    def test_note_has_title(self):
        self.assertEqual(self.note.title, "Test Note")

    def test_note_has_content(self):
        self.assertEqual(self.note.content, "This is a test note")

    def test_note_can_be_updated(self):
        self.note.title = "Updated Test Note"
        self.note.content = "This is an updated test note"
        self.note.save()
        self.assertEqual(self.note.title, "Updated Test Note")
        self.assertEqual(self.note.content, "This is an updated test note")

    def test_note_can_be_deleted(self):
        self.note.delete()
        self.assertEqual(Note.objects.all().count(), 0)
