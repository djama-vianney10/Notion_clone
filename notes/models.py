from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name

class Operation(models.Model):
    STATUS_CHOICES = [
        ('attente', 'En attente'),
        ('en_cours', 'En cours'),
        ('termine', 'Terminé'),
        ('bloque', 'Bloqué'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='operations')
    created_at = models.DateTimeField(auto_now_add=True) # Date d'ajout
    title = models.CharField(max_length=200) # Tâche / Amélioration
    problem_description = models.TextField() # Contexte précis
    proposed_solution = RichTextField() # Approche technique
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='attente')
    tags = models.ManyToManyField(Tag, related_name='operations', blank=True)

    def __str__(self):
        return self.title