from django.db import models

class Staff(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    position = models.CharField(max_length=100)
    hire_date = models.DateField()

    def __str__(self):
        return self.name
