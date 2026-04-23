from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Operation, Tag
from ckeditor.widgets import CKEditorWidget

# Formulaire d'inscription (indispensable pour ta vue register)
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']

# Formulaire technique
class OperationForm(forms.ModelForm):
    class Meta:
        model = Operation
        fields = ['title', 'problem_description', 'proposed_solution', 'start_date', 'end_date', 'status', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Correction bug paiement Wave'}),
            'problem_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Décrivez le contexte...'}),
            'proposed_solution': CKEditorWidget(),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'tags': forms.CheckboxSelectMultiple(attrs={'class': 'tag-list-checkbox'}),
        }