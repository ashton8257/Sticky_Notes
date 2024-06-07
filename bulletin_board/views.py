# bulletin_board/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm


# Create your views here.
# Define the function to return the list of posts
def post_list(request):
    # Retrieve all posts
    posts = Post.objects.all()
    # Render the HTML template with the context of the posts
    return render(request, 'bulletin_board/post_list.html', {'posts': posts})


# Define the function to show the detail of the post
def post_detail(request, pk):
    # Retrieve the post with the given primary key
    post = get_object_or_404(Post, pk=pk)
    # Render the HTML template with the context of the post
    return render(request, 'bulletin_board/post_detail.html', {'post': post})


# Define the function to create a post
def post_create(request):
    # If the request method is POST, process the data
    if request.method == 'POST':
        # Create a new instance of form with the data
        form = PostForm(request.POST)
        # If the form is valid, save it with the data
        if form.is_valid():
            form.save()
            # Redirect the user back to the list of posts when saved
            return redirect('post_list')
    # If the request method is not POST, create a new form
    else:
        form = PostForm()
    # Render the HTML template with the context of the post
    return render(request, 'bulletin_board/post_form.html', {'form': form})


# Define the function to edit a post
def post_edit(request, pk):
    # Retrieve the post with the primary key
    post = get_object_or_404(Post, pk=pk)
    # If the request method is POST, process the data
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        # If the form is valid, save the updated form
        if form.is_valid():
            form.save()
            # Redirect the user the the list of posts
            return redirect('post_list')
    # If the request method is not POST, create a new form
    else:
        form = PostForm(instance=post)
    # Render the HTML template with the form's context
    return render(request, 'bulletin_board/post_form.html', {'form': form})


# Define the function to delete a post
def post_delete(request, pk):
    # Retrieve the post with the primary key
    post = get_object_or_404(Post, pk=pk)
    # If the request method is POST, delete the post
    if request.method == 'POST':
        post.delete()
        # Redirect user to list of post
        return redirect('post_list')
    # Render the post_confirm_delete template with the context of the respective post
    return render(request, 'bulletin_board/post_confirm_delete.html', {'post': post})
