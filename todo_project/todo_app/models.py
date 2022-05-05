from django.db import models

# Create your models here.


class NameUser(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class MyUser(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name


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
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.task_title
