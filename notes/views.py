from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.db.models import Count, Q
from django.utils import timezone
from .models import Note, Tag
from .forms import NoteForm, RegisterForm




def index(request):
    return render(request, 'notes/index.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Compte créé avec succès !')
            return redirect('note_list')
    else:
        form = RegisterForm()
    return render(request, 'notes/register.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'Vous avez été déconnecté avec succès !')
        return redirect('index')
    return render(request, 'notes/logout.html')


@login_required
def dashboard(request):
    # Récupérer les statistiques pour l'utilisateur connecté
    total_notes = Note.objects.filter(user=request.user).count()
    notes_this_month = Note.objects.filter(
        user=request.user,
        created_at__month=timezone.now().month
    ).count()

    notes_terminees = Note.objects.filter(user=request.user, resultat='termine').count()
    notes_en_cours = Note.objects.filter(user=request.user, resultat='en_cours').count()

    notes_per_tag = Tag.objects.annotate(
        notes_count=Count('notes', filter=Q(notes__user=request.user))
    ).values('name', 'notes_count')

    total_tags = Tag.objects.count()
    context = {
        'total_notes': total_notes,
        'notes_this_month': notes_this_month,
        'notes_terminees': notes_terminees,
        'notes_en_cours': notes_en_cours,
        'notes_per_tag': list(notes_per_tag),
        'total_tags': total_tags,
    }
    return render(request, 'notes/dashboard.html', context)


@login_required
def note_list(request):
    notes = Note.objects.filter(user=request.user)
    return render(request, 'notes/note_list.html', {'notes': notes})

@login_required
def note_create(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            form.save_m2m()  # Pour sauvegarder les relations ManyToMany (tags)
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'notes/note_form.html', {'form': form})

@login_required
def note_edit(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save()
            return redirect('note_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_form.html', {'form': form})

@login_required
def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    note.delete()
    return redirect('note_list')

