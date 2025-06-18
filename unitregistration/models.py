from django.db import models
from courseregistration.models import Course

class Unit(models.Model):
    title = models.CharField(max_length=100)
    unit_code = models.CharField(max_length=10, unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='units')

    def __str__(self):
        return self.title
