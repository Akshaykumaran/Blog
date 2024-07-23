from django.db import models

# Create your models here.

class Project(models.Model):
    project_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.project_name
    
class Task(models.Model):
    STATUS_CHOICES = [
        ('not started', 'Not Started'),
        ('in progress', 'In Progress'),
        ('Incomplete', 'Incomplete'),
        ('completed', 'Completed'),
    ]
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)
    task_name =models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)  # Use choices here
    due_date = models.DateField()

    def __str__(self) -> str:
        return self.task_name