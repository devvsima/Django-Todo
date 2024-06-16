from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.decorators import login_required
from .forms import TodoForm
from .models import TodoList
# Create your views here.
def index(request) -> HttpResponse:
    todolist = TodoList.objects.filter(user=request.user)
    context = {
        "title": 'Online Organizer',
        "todolist": todolist,
        
    }

    
    return render(request, 'todo/todo.html', context)


@login_required
def all_todo(request):
    todos = TodoList.objects.filter(user=request.user).order_by('-created')
    return render(request, 'todo/todo.html', {'todos':todos})

@login_required
def done_todo(request):
    todos = TodoList.objects.filter(user=request.user).order_by('-due_date')
    return render(request, 'todo/todo.html', {'todos':todos})

@login_required
def delete_todo(request, todo_pk):
    todo = get_object_or_404(TodoList, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('currenttodos')
    
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
            print('ale3')
            
            return redirect('todo:currenttodos')
        else:
            return render(request, 'todo/create_todo.html', {'form': form, 'error': 'Неверно заполненное поле'})
        # except ValueError:
        #     return render(request, 'todo/create_todo.html', {'form': TodoForm(), 'error': 'Неверно заполненное поле'})



@login_required
def viewtodo(request, todo_pk):
    todo = get_object_or_404(TodoList, pk=todo_pk, user=request.user)
    form = TodoForm(instance=todo)
    if request.method == 'GET':
        form = TodoForm(instance=todo)
        return render(request, 'todo/viewtodo.html', {'todo':todo, 'form':form})
    else:
        try:
            form = TodoForm(request.POST, instance=todo)
            form.save()
            return redirect('todo:currenttodos')

        except ValueError:
            return render(request, 'todo/view.html', {'form':todo, 'error':'неверно заполненое поле'})

@login_required
def deletetodo(request, todo_pk):
    todo = get_object_or_404(TodoList, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo:currenttodos')
    
    
@login_required
def currenttodos(request):
    todos = TodoList.objects.filter(user=request.user, ).order_by('-created')
    return render(request, 'todo/todo.html', {'todolist':todos})