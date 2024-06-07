# sticky_notes_app/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm


# Create your views here.
# Define the function to return the list of notes
def note_list(request):
    # Retrieve all notes
    notes = Note.objects.all()
    # Render the HTML template with the context of the notes
    return render(request, 'sticky_notes_app/note_list.html', {'notes': notes})


# Define the function to show the detail of the note
def note_detail(request, pk):
    # Retrieve the note with the given primary key
    note = get_object_or_404(Note, pk=pk)
    # Render the HTML template with the context of the note
    return render(request, 'sticky_notes_app/note_detail.html', {'note': note})


# Define the function to create a note
def note_create(request):
    # If the request method is POST, process the data
    if request.method == 'POST':
        # Create a new instance of form with the data
        form = NoteForm(request.POST)
        # If the form is valid, save it with the data
        if form.is_valid():
            form.save()
            # Redirect the user back to the list of notes when saved
            return redirect('note_list')
    # If the request method is not POST, create a new form
    else:
        form = NoteForm()
    # Render the HTML template with the context of the note
    return render(request, 'sticky_notes_app/note_form.html', {'form': form})


# Define the function to edit a note
def note_edit(request, pk):
    # Retrieve the note with the primary key
    note = get_object_or_404(Note, pk=pk)
    # If the request method is POST, process the data
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        # If the form is valid, save the updated form
        if form.is_valid():
            form.save()
            # Redirect the user the the list of notes
            return redirect('note_list')
    # If the request method is not POST, create a new form
    else:
        form = NoteForm(instance=note)
    # Render the HTML template with the form's context
    return render(request, 'sticky_notes_app/note_form.html', {'form': form})


# Define the function to delete a note
def note_delete(request, pk):
    # Retrieve the note with the primary key
    note = get_object_or_404(Note, pk=pk)
    # If the request method is POST, delete the note
    if request.method == 'POST':
        note.delete()
        # Redirect user to list of notes
        return redirect('note_list')
    # Render the note_confirm_delete template with the context of the respective note
    return render(request, 'sticky_notes_app/note_confirm_delete.html', {'note': note})
