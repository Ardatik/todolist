from django.db import models
from account.models import CustomUser
import uuid


class List_model(models.Model):

    PRIORITY_CHOICES = [
        ('High', 'Высокий'),
        ('Mid', 'Средний'),
        ('Low', 'Низкий'),
    ]
    prioritet = models.CharField(max_length=20, choices=PRIORITY_CHOICES)
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE)
    day_tasks = models.TextField()
    completed_task = models.BooleanField(default=False)
    date_create = models.DateTimeField(auto_now=True)
    date_start = models.DateField(default=None,blank=True,null=True)
    date_finish = models.DateField(default=None,blank=True,null=True)

    class Meta:
        ordering = ["-date_create"]

    def __str__(self):
        return self.day_tasks
