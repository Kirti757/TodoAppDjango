from django.db import models

# Create your models here.
class Tasks(models.Model):
    taskname=models.TextField()



    def __str__(self):
        return self.taskname