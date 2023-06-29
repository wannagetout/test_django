from datetime import date

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound, request
from .models import Tasks


def get_all_tasks(request) -> render:
    tasks = Tasks.objects.all()
    print(request.GET)
    if request.GET.get('status-filter'):
        filter_tasks = tasks.filter(status=request.GET.get('status-filter'))
        return render(request, 'task.html', {'tasks': filter_tasks})
    else:
        return render(request, 'task.html', {'tasks': tasks})

def create_task(request) -> render:
    if request.method == 'POST':
        task = Tasks()
        task.description = request.POST.get('description')
        if request.POST.get('status'):
            task.status = True
        else:
            task.status = False
        task.save()
    return HttpResponseRedirect('/tasks')

def update_task(request, id: int) -> render:
    try:
        task = Tasks.objects.get(id=id)
        if request.method == 'POST':
            task.description = request.POST.get('description')
            if request.POST.get('status'):
                task.status = True
            else:
                task.status = False
            task.update_date = date.today()
            task.save()
            return HttpResponseRedirect('/tasks')
        else:
            return render(request, 'edit.html', {'task': task})
    except Tasks.DoesNotExist:
        return HttpResponseNotFound("<p>Такая задача не найдена</p>")

def delete_task(request, id: int) -> render:
    try:
        task = Tasks.objects.get(id=id)
        task.delete()
        return HttpResponseRedirect('/tasks')
    except Tasks.DoesNotExist:
        return HttpResponseNotFound("<p>Такая задача не найдена</p>")
