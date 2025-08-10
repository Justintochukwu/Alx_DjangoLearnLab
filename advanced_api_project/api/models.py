from django.db import models

# Author model represents a writer in our system.
# Each Author can have multiple related books (one-to-many relationship).
class Author(models.Model):
    name = models.CharField(max_length=255)  # Author's name

    def __str__(self):
        return self.name

# Book model represents a published book written by an Author.
# It contains the book title, year of publication, and a link to its author
class Book(models.Model):
    title = models.CharField(max_length=255)  # Book's title
    publication_year = models.IntegerField()  # Year of publication
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,  # If author is deleted, delete related books
        related_name='books'  # Enables reverse lookup: author.books.all()
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"