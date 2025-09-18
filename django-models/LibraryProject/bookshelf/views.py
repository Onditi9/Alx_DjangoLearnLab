# Create your views here.
from . import BookForm

def create_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return ("book_list")
    else:
        form = BookForm()
    return (request, "bookshelf/form_example.html", {"form": form})
