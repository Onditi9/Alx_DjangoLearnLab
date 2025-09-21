from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()



    def _str_(self):
        return f"{self.title} by {self.author} ({self.publication_year})"



# Create your models here