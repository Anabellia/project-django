from django.db import models

# Create your models here.

class Todo(models.Model):
    URGENT_PRIORITY = 'U'
    HIGH_PRIORITY = 'H'
    MEDIUM_PRIORITY = 'M'
    LOW_PRIORITY = 'L'

    TASK_PRIORITY_CHOICES = [
        (URGENT_PRIORITY, 'Urgent'),
        (HIGH_PRIORITY, 'High'),
        (MEDIUM_PRIORITY, 'Medium'),
        (LOW_PRIORITY, 'Low')
    ]
    task_title = models.CharField(max_length=100)
    task_priority = models.CharField(
        max_length=1,
        choices=TASK_PRIORITY_CHOICES,
        default=MEDIUM_PRIORITY,
    )
