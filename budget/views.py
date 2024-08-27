from django.shortcuts import render, redirect
from datetime import date
from .models import BudgetEntry
from .forms import BudgetEntryForm

def budget_entries(request):
    today = date.today()
    user = request.user
    entries = BudgetEntry.objects.all()
    if request.method == "POST":
        form = BudgetEntryForm(request.POST)
        if form.is_valid():
            form.save()
            latest_created_entry = entries.latest("created")
            latest_created_entry.owner = user.username
            latest_created_entry.save()
            context = {'entries':entries, 'form':form, 'user':user.username, 'today':today}
            return render(request, 'budget/list.html', context)
    else:
        form = BudgetEntryForm()
        context = {'entries':entries, 'form':form, 'user':user.username, 'today':today}
        return render(request, 'budget/list.html', context)


def update_entry(request, pk):
	entry = BudgetEntry.objects.get(id=pk)
	form = BudgetEntryForm(instance=entry)

	if request.method == 'POST':
		form = BudgetEntryForm(request.POST, instance=entry)
		if form.is_valid():
			form.save()
			return redirect('/budget')

	context = {'form':form}

	return render(request, 'budget/update.html', context)


def delete_entry(request, pk):
	entry = BudgetEntry.objects.get(id=pk)
	entry.delete()
	return redirect('/budget')