from django.db import models

# Create your models here.

from django.db import models

class Author(models.Model):
    """
    Author model to store book authors.
    - name: string field representing the author's name.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model to store book details.
    - title: title of the book.
    - publication_year: year the book was published.
    - author: ForeignKey linking each book to a specific author.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
