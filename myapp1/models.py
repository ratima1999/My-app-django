from django.db import models

class MyModel(models.Model):
    field1 = models.CharField(max_length=50)
    field2 = models.IntegerField()
    class MyModel(models.Model): 
        name = models.CharField(max_length=50)
        class MyModel(models.Model): 
          description = models.TextField()
          class MyModel(models.Model): 
             price = models.FloatField()
             class MyModel(models.Model):
               is_available = models.BooleanField()
               class MyModel(models.Model): 
                 created_at = models.DateTimeField(auto_now_add=True)
class Author(models.Model): 
 name = models.CharField(max_length=50) 
class Book(models.Model): 
 title = models.CharField(max_length=100) 
author = models.ForeignKey(Author, on_delete=models.CASCADE)








