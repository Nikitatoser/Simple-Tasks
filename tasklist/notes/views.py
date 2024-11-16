from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Notes
from .forms import NoteForm
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string

@login_required
def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return redirect('login')


@login_required
def note_list(request):
    notes = Notes.objects.filter(user=request.user)
    return render (request, 'notes/note_list.html', {'notes': notes})

@login_required
def note_detail(request, pk):
    note = get_object_or_404(Notes, pk=pk, user=request.user)
    return render(request, 'notes/note_detail.html', {'note': note})

@login_required
def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True}, status=200)
            return redirect('notes:note_list')
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': False,
                    'errors': render_to_string('notes/form_errors.html', {'form': form})
                }, status=400)
    else:
        form = NoteForm()
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            html = render_to_string('notes/note_form.html', {'form': form}, request=request)
            return HttpResponse(html)
    return render(request, 'notes/note_form.html', {'form': form})



@login_required
def note_update(request, pk):
    note = get_object_or_404(Notes, pk=pk)

    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save() 
            return redirect("notes:note_list") 
    else:
        form = NoteForm(instance=note) 

    return render(request, 'notes/note_form.html', {'form': form})



@login_required
def note_delete(request, pk):
    note = get_object_or_404(Notes, pk=pk, user = request.user)
    user = request.user
    if request.method == 'POST':
        note.delete()
        return redirect('notes:note_list')
    return render(request, 'notes/note_list.html', {'note': note, 'user': user})

        