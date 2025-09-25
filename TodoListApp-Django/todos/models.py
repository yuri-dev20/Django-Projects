from django.db import models

# Create your models here.
class Todo(models.Model):
    todo_name = models.CharField(max_length=100)
    added_date = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.todo_name