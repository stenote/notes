from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
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
        passwd = request.POST['passwd']
        note = Note(title=title, text=text, passwd=passwd)

        if len(passwd):
            request.session[note_ref] = True

        note.save()

        return HttpResponseRedirect(reverse('notes:view', args=(note.ref, )))
    else:
        return render(request, 'add.html')

def edit(request, note_ref):

    note = get_object_or_404(Note, ref=note_ref)

    if request.method == 'POST':
        text = request.POST['text']
        title = text.split('\n')[0].strip('# ')
        passwd = request.POST['passwd']

        note.text = text
        note.title = title
        note.passwd = passwd

        if len(passwd):
            request.session[note_ref] = True

        note.save()

        return HttpResponseRedirect(reverse('notes:view', args=(note.ref, )))

    return render(request, 'edit.html', {
        'note': note
    })


def delete(request, note_ref):

    note = get_object_or_404(Note, ref=note_ref)

    note.delete()

    return HttpResponseRedirect(reverse('notes:list'))


def view(request, note_ref):

    note = get_object_or_404(Note, ref=note_ref)

    note_passwd_len = len(note.passwd)

    if request.method == 'POST' and note.passwd == request.POST['passwd']:

        request.session[note_ref] = True


    if note_passwd_len == 0 or note_ref in request.session:

        return render(request, 'view.html', {
            'note': note
        })

    return HttpResponse(render(request, 'passwd.html'), status=401)
