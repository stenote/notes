from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse


from .models import Note

# Create your views here.


def list(request):

    return render(request, 'list.html', {
        'notes': Note.objects.order_by('-id'),
    })


def add(request):

    if request.method == 'POST':

        text = request.POST['text']
        title = text.split('\n')[0].strip('# ')
        note = Note(title=title, text=text)

        note.save()

        return HttpResponseRedirect(reverse('notes:view', args=(note.id, )))
    else:
        return render(request, 'add.html')


def view(request, note_id):

    note = get_object_or_404(Note, pk=note_id)

    return render(request, 'view.html', {
        'note': note
    })