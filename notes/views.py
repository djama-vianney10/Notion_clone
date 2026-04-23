from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.db.models import Count, Q
from django.utils import timezone
from .models import Operation, Tag
from .forms import OperationForm, RegisterForm




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
    user_ops = Operation.objects.filter(user=request.user)
    
    # Statistiques
    stats = {
        'total': user_ops.count(),
        'termine': user_ops.filter(status='termine').count(),
        'en_cours': user_ops.filter(status='en_cours').count(),
        'bloque': user_ops.filter(status='bloque').count(),
        'attente': user_ops.filter(status='attente').count(),
    }

    tags_data = Tag.objects.annotate(
        count=Count('operations', filter=Q(operations__user=request.user))
    ).filter(count__gt=0).values('name', 'count')

    return render(request, 'notes/dashboard.html', {
        'stats': stats,
        'tags_data': list(tags_data),
    })

@login_required
def note_list(request):
    operations = Operation.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'notes/note_list.html', {'operations': operations})

@login_required
def note_create(request):
    if request.method == "POST":
        form = OperationForm(request.POST)
        if form.is_valid():
            op = form.save(commit=False)
            op.user = request.user
            op.save()
            form.save_m2m()
            return redirect('note_list')
    else:
        form = OperationForm()
    return render(request, 'notes/note_form.html', {'form': form})

@login_required
def note_edit(request, pk):
    op = get_object_or_404(Operation, pk=pk, user=request.user)
    if request.method == "POST":
        form = OperationForm(request.POST, instance=op)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = OperationForm(instance=op)
    return render(request, 'notes/note_form.html', {'form': form})

@login_required
def note_delete(request, pk):
    operation = get_object_or_404(Operation, pk=pk, user=request.user)
    operation.delete()
    messages.success(request, "L'opération a été supprimée avec succès.")
    return redirect('note_list')

