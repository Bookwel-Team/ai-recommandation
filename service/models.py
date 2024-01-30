from django.db import models


class Book(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    file_link = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    STATUS_CHOICES = [
        ('ADMIN', 'Admin'),
        ('CLIENT', 'Client'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
