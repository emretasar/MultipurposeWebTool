from django.shortcuts import render, redirect
from datetime import date
from .models import Note
from .forms import NoteForm

def notes(request):
    today = date.today()
    user = request.user
    notes = Note.objects.all()
    if request.method == "POST":
        form = NoteForm(request.POST)
        temp = request.POST['tag']
        print(temp)	
        print(type(temp))	
        if form.is_valid():
            form.save()
            latest_created_note = notes.latest("create_date")
            latest_created_note.owner = user.username
            latest_created_note.save()
            context = {'notes':notes, 'form':form, 'user':user.username, 'today':today}
            return render(request, 'notes/list.html', context)
    else:
        form = NoteForm()
        context = {'notes':notes, 'form':form, 'user':user.username, 'today':today}
        return render(request, 'notes/list.html', context)


def update_note(request, pk):
	note = Note.objects.get(id=pk)
	form = NoteForm(instance=note)

	if request.method == 'POST':
		form = NoteForm(request.POST, instance=note)
		if form.is_valid():
			form.save()
			return redirect('/notes')

	context = {'form':form}

	return render(request, 'notes/update.html', context)


def delete_note(request, pk):
	note = Note.objects.get(id=pk)
	note.delete()
	return redirect('/notes')