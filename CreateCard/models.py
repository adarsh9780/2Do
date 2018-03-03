from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class ToDoModel(models.Model):
    name = models.CharField(max_length=40)
    time = models.DateTimeField()
    to_do = models.TextField()

    def __str__(self):
        return self.to_do