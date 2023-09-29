from django.shortcuts import render, redirect
from datetime import date
from .models import Task
from .forms import TaskForm

def todos(request):
	today = date.today()
	user = request.user
	tasks = Task.objects.all()
	if request.method == "POST":
		form = TaskForm(request.POST)	
		if form.is_valid():
			form.save()
			latest_created_task = tasks.latest("created")
			latest_created_task.owner = user.username
			latest_created_task.save()
			context = {'tasks':tasks, 'form':form, 'user':user.username, 'today':today}
			return render(request, 'todo/list.html', context)
	else:
		form = TaskForm()
		context = {'tasks':tasks, 'form':form, 'user':user.username, 'today':today}
		return render(request, 'todo/list.html', context)


def updateTask(request, pk):
	task = Task.objects.get(id=pk)
	form = TaskForm(instance=task)

	if request.method == 'POST':
		form = TaskForm(request.POST, instance=task)
		if form.is_valid():
			form.save()
			return redirect('/todos')

	context = {'form':form}

	return render(request, 'todo/update.html', context)


def deleteTask(request, pk):
	item = Task.objects.get(id=pk)
	item.delete()
	return redirect('/todos')