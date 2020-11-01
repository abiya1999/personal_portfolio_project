from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100) #title for a project can not be more than 100
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True) #not neccesarily needed thatsy

    def __str__(self):
        return self.title

class Course(models.Model):
    title = models.CharField(max_length=100) #title for a project can not be more than 100
    description = models.CharField(max_length=250)
    url = models.URLField(blank=True) #not neccesarily needed thatsy

    def __str__(self):
        return self.title
