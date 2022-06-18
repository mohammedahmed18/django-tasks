from django.db import models
from django.utils.html import mark_safe

class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    def __str__(self):
        return self.first_name + ' ' + self.last_name
 

class Book(models.Model):
    name = models.CharField(max_length=200)
    department = models.ForeignKey(
        'Department',
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.name


class Department(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    def __str__(self):
        return self.first_name + ' ' + self.last_name
 

class ImageCollection(models.Model):
    image_name = models.CharField(max_length=200)
    image_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image_file = models.ImageField(upload_to='static/uploads')
    
    def __str__(self):
       return self.image_name
 