from django.db import models


class Book(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    file_link = models.CharField(max_length=255)

    def __str__(self):
        return self.title
