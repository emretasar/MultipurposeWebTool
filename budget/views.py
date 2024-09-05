from django.shortcuts import render, redirect
from datetime import date
from .models import BudgetEntry
from .forms import BudgetEntryForm, FilterForm

def budget_entries(request):
    today = date.today()
    user = request.user


    entries = BudgetEntry.objects.all()
    # entries = BudgetEntry.objects.filter(category = "Yemek")
    # entries = BudgetEntry.objects.filter(date__month = 1)
    # entries = BudgetEntry.objects.filter(inout = "Invest")
    # entries = BudgetEntry.objects.filter(inout = _income_or_expense, date__month = _month, category=_category)
    
    if request.method == "POST":
        filterForm = FilterForm(request.POST)
        if filterForm.is_valid():
            _income_or_expense = filterForm.cleaned_data['income_or_expense']
            _month = filterForm.cleaned_data['month']
            _category = filterForm.cleaned_data['category']
            print(_income_or_expense)
            print(_month)
            print(_category)
            entries = BudgetEntry.objects.filter(category = _category)
            context = {'entries':entries, 'filterForm':filterForm, 'user':user.username, 'today':today}
            return render(request, 'budget/list.html', context)
        else:
            print("Not Valid Form")
        form = BudgetEntryForm(request.POST)
        if form.is_valid():
            form.save()
            latest_created_entry = entries.latest("created")
            latest_created_entry.owner = user.username
            latest_created_entry.save()
            context = {'entries':entries, 'form':form, 'user':user.username, 'today':today}
            return render(request, 'budget/list.html', context)
        else:
            print("Not Valid Form")
        

    else:
        form = BudgetEntryForm()
        filterForm = FilterForm()
        context = {'entries':entries, 'form':form, 'filterForm': filterForm, 'user':user.username, 'today':today}
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