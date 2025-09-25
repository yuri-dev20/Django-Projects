from django.urls import path

from . import views

app_name = "todos"

urlpatterns = [
    path("", views.todo_list, name="todo_list"),
    path("complete/<int:todo_id>/", views.complete, name="complete"),
    path("delete/<int:todo_id>/", views.delete, name="delete"),
]