from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

statuses = (
    ('NOT DONE','NOT DONE'),
    ('DONE','DONE'),

)

# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name

class Status(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    todo = models.ForeignKey(Todo,on_delete=models.CASCADE)
    status = models.CharField(max_length=255,
                            choices=statuses,default='NOT DONE')
    changed_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.todo.name




