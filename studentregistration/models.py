from django.db import models

class student(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    course = models.CharField(max_length=100)
    admission_date = models.DateField()

    def __str__(self):
        return self.fullname

class staff(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    department = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    joining_date = models.DateField()

    def __str__(self):
        return self.fullname

class course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    duration = models.IntegerField(help_text='Duration in months')
    description = models.TextField()
    coordinator = models.ForeignKey(staff, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.code} - {self.name}'

class unit(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    course = models.ForeignKey(course, on_delete=models.CASCADE, related_name='units')
    instructor = models.ForeignKey(staff, on_delete=models.SET_NULL, null=True)
    credits = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return f'{self.code} - {self.name}'
