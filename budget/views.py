from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import date
from .models import BudgetEntry, FilterFormModel
from .forms import BudgetEntryForm, FilterForm
import openpyxl


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
            # try without here later
            if _month:
                currentYear = date.today().year
                entries = entries.filter(date__year = currentYear)
                entries = entries.filter(date__month = FilterFormModel.MONTH_CHOICES.index((_month, _month))+1)
            if _category:
                entries = entries.filter(category =_category)
            
            global filtered_entries
            filtered_entries = entries.order_by("date")

        if form.is_valid():
            # Save form but do not commit to the database yet (owner needs to be set)
            new_entry = form.save(commit=False)
            new_entry.owner = user.username  # Assign owner before saving
            new_entry.save()

        entries_to_display = entries.order_by("-date")[:10]
        context = {'entries': entries_to_display, 'form': form, 'filterForm': filterForm, 'user': user.username, 'today': today}
        return render(request, 'budget/list.html', context)

    # Handle GET request
    else:
        form = BudgetEntryForm()
        filterForm = FilterForm()
        entries_to_display = entries.order_by("-date")[:10]
        context = {'entries': entries_to_display, 'form': form, 'filterForm': filterForm, 'user': user.username, 'today': today}
        return render(request, 'budget/list.html', context)

def export_to_excel(request):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = 'Exported Data'

    columns = ['Income/Expense', 'Amount', 'Date', 'Category', 'Description']
    ws.append(columns)  # Append headers

    entries = filtered_entries
    for entry in entries:
        if (entry.inout == "Outcome" or entry.inout == "Invest"): 
            entry.amount *= -1
        ws.append([entry.inout, entry.amount, entry.date, entry.category, entry.description])

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="exported_data.xlsx"'

    wb.save(response)
    
    return response

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
