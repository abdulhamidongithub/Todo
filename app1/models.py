from django.db import models

class Plan(models.Model):
    sarlavha = models.CharField(max_length=100)
    vaqt = models.DateField()
    batafsil = models.TextField()
    status = models.CharField(max_length=100)
    def __str__(self):
        return self.sarlavha

