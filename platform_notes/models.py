# Django has a relatively easy to use Object Relationship Mapper (ORM) to help us make queries simply and cleanly. We've already reviewed why ORM's make our code easier to read and understand. Now we'll show you how to use one in a bit more depth.

# The Objects object (what?)
# Django models are built to communicate with views via an attribute called objects. The objects attribute is an object itself and has methods for each common database query. This objects attribute allows us to run queries for each table from our view file. Let's investigate how that works.

# We'll start with the User class from our models.py file.

# In models.py

from __future__ import unicode_literals
from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


class User(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
    return self.first_name + " " + self.last_name

# NOTES: 
# class User(models.Model):
#     name = models.CharField()
#     password = models.CharField()
# class Item(models.Model):
#     itemname = models.CharField()
#     user = models.ForeignKey(User, related_name="items")
# item."class_attribute"
# user."related_name" 