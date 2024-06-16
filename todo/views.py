from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.decorators import login_required
from .forms import TodoForm
from .models import TodoList
# Create your views here.



@login_required
def create_todo(request):
    if request.method == 'GET':
        return render(request, 'todo/create_todo.html', {'form': TodoForm()})
    else:
        print('ale')
        # try:
        form = TodoForm(request.POST, request.FILES)  # Используем правильный класс формы и добавляем request.FILES
        if form.is_valid():
            print('ale2')
            
            newtodo = form.save(commit=False)
            newtodo.user = request.user
            newtodo.save()
            
            return redirect('todo:current')
        else:
            return render(request, 'todo/create_todo.html', {'form': form, 'error': 'Неверно заполненное поле'})
        # except ValueError:
        #     return render(request, 'todo/create_todo.html', {'form': TodoForm(), 'error': 'Неверно заполненное поле'})

@login_required
def edit_todo(request, task_id):
    todo = get_object_or_404(TodoList, id=task_id, user=request.user)
    if request.method == 'GET':
        form = TodoForm(instance=todo)
        return render(request, 'todo/edit_todo.html', {'form': form, 'todo': todo})
    else:
        try:
            form = TodoForm(request.POST, request.FILES, instance=todo)
            if form.is_valid():
                form.save()
                return redirect('todo:current')
            else:
                return render(request, 'todo/edit_todo.html', {'form': form, 'todo': todo, 'error': 'Неверно заполненное поле'})
        except ValueError:
            return render(request, 'todo/edit_todo.html', {'form': form, 'todo': todo, 'error': 'Неверно заполненное поле'})
        
@login_required
def mark_as_done(request, task_id):
    todo = TodoList.objects.filter(id=task_id)
    todo.update(done=True)
    return redirect('todo:current')

@login_required
def mark_as_current(request, task_id):
    todo = TodoList.objects.filter(id=task_id)
    todo.update(done=False)
    return redirect('todo:done')

@login_required
def delete_todo(request, task_id):
    todo = TodoList.objects.filter(id=task_id)
    todo.delete()
    return redirect('todo:current')
    
# ---------------------------------------------------------------------
    
@login_required
def current_todo(request):
    todos = TodoList.objects.filter(user=request.user, done=False).order_by('-created')
    context = {
        'name':'Current',
        'todolist':todos
    }
    return render(request, 'todo/todo.html', context)

@login_required
def all_todo(request):
    todos = TodoList.objects.filter(user=request.user).order_by('-created')
    context = {
        'name':'All',
        'todolist':todos
    }
    return render(request, 'todo/todo.html', context)

@login_required
def done_todo(request):
    todos = TodoList.objects.filter(user=request.user, done=True)
    context = {
        'name':'Done',
        'todolist':todos
    }
    return render(request, 'todo/todo.html', context)
