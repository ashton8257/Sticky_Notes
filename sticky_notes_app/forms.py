# sticky_notes_app/forms.py
from django import forms
from .models import Note


# NoteForm class contains the model and the fields
class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']
