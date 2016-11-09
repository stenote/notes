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

        return HttpResponseRedirect(reverse('notes:view', args=(note.ref, )))
    else:
        return render(request, 'add.html')


def delete(request, note_ref):

    note = get_object_or_404(Note, ref=note_ref)

    note.delete()

    return HttpResponseRedirect(reverse('notes:list'))


def view(request, note_ref):

    note = get_object_or_404(Note, ref=note_ref)

    return render(request, 'view.html', {
        'note': note
    })