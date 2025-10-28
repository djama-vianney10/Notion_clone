from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Note(models.Model):
    STATUS_CHOICES = [
        ('en_cours', 'En cours'),
        ('termine', 'Terminé'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes', null=True)
    title = models.CharField(max_length=100)
    content = RichTextField()
    tags = models.ManyToManyField('Tag', related_name='notes', blank=True)  # Association avec les tags
    created_at = models.DateTimeField(auto_now_add=True)
    resultat = models.CharField(max_length=10, choices=STATUS_CHOICES, default='en_cours')

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

