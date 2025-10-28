from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from ckeditor.widgets import CKEditorWidget
from .models import Note, Tag

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class NoteForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    content = forms.CharField(widget=CKEditorWidget())
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all().order_by('name'),
        widget=forms.SelectMultiple(attrs={
            'class': 'form-select',
            'style': 'width: 100%'
        }),
        required=False,
        help_text='Sélectionnez un ou plusieurs tags'
    )
    resultat = forms.ChoiceField(
        choices=[('en_cours', 'En cours'), ('termine', 'Terminé')],
        widget=forms.Select(attrs={'class': 'form-select'}),
        initial='en_cours'
    )

    class Meta:
        model = Note
        fields = ['title', 'content', 'tags', 'resultat']
