from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from .models import Todo

# Create your views here.
def todo_list(request):
    status = request.GET.get("status", "not_completed")

    if status == "completed":
        todos = Todo.objects.filter(is_completed=True)

    else:
        todos = Todo.objects.filter(is_completed=False)

    if request.method == "POST":
        todo_name = request.POST.get("todo_name")
        
        if todo_name:
            Todo.objects.create(todo_name=todo_name)
            return redirect("todos:todo_list")
        
    return render(
        request,
        "todos/todo_list.html",
        {
            "todos": todos,
            "status": status
        }
    )

def complete(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)

    todo.is_completed = True
    todo.save()
    return redirect("todos:todo_list")

def delete(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.delete()
    return redirect("todos:todo_list")