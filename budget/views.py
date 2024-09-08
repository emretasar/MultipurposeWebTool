from django.shortcuts import render, redirect
from datetime import date
from .models import BudgetEntry, FilterFormModel
from .forms import BudgetEntryForm, FilterForm

def budget_entries(request):
    today = date.today()
    user = request.user
    entries = BudgetEntry.objects.all()

    # Handle POST Request
    if request.method == "POST":
        filterForm = FilterForm(request.POST)
        form = BudgetEntryForm(request.POST)

        if filterForm.is_valid():
            # Apply filters based on the FilterForm data
            _income_or_expense = filterForm.cleaned_data['income_or_expense']
            _month = filterForm.cleaned_data['month']
            _category = filterForm.cleaned_data['category']
            
            if _income_or_expense:
                entries = entries.filter(inout =_income_or_expense)
            if _month:
                entries = entries.filter(date__month = FilterFormModel.MONTH_CHOICES.index((_month, _month))+1)
            if _category:
                entries = entries.filter(category =_category)

        if form.is_valid():
            # Save form but do not commit to the database yet (owner needs to be set)
            new_entry = form.save(commit=False)
            new_entry.owner = user.username  # Assign owner before saving
            new_entry.save()

            # return redirect('/budget')  # Redirect after successful submission

        else:
            print("Form not valid")

        # If either form fails, re-render the template with the forms and entries
        context = {'entries': entries, 'form': form, 'filterForm': filterForm, 'user': user.username, 'today': today}
        return render(request, 'budget/list.html', context)

    # Handle GET request
    else:
        form = BudgetEntryForm()
        filterForm = FilterForm()
        context = {'entries': entries, 'form': form, 'filterForm': filterForm, 'user': user.username, 'today': today}
        return render(request, 'budget/list.html', context)


def update_entry(request, pk):
    entry = BudgetEntry.objects.get(id=pk)
    form = BudgetEntryForm(instance=entry)

    if request.method == 'POST':
        form = BudgetEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('/budget')

    context = {'form': form}
    return render(request, 'budget/update.html', context)


def delete_entry(request, pk):
    entry = BudgetEntry.objects.get(id=pk)
    entry.delete()
    return redirect('/budget')
