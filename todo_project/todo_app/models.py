from django.db import models

# Create your models here.


class UserManager(models.Manager):
    def create_user(self, firstname, lastname):
        user = self.create(first_name=firstname, last_name=lastname)
        return user


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    objects = UserManager()

    def __str__(self):
        return self.first_name


user2 = User.objects.create_user('Paja', 'Patak')


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
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.task_title
