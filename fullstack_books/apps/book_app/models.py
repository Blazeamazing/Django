from __future__ import unicode_literals
from django.db import models

# Create your models here.
class AuthorManager(models.Manager):
    def createAuthor(self, form_data):
        name = form_data['name']
        author = Author.objects.create(name=name)
        
        return author

class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
#these two classes are currently not attatched so I am going to need a      relationship between them.
#need to validate date using this model manager. classname then Manager.
    objects = AuthorManager()

class BookManager(models.Manager):
    #so now inside here we can define our own customized methods for handling anything we want inside of our model.
    def validate(self, form_data):
    #now need to set up what i am validating for...
        errors = []

        if len(form_data['name'])== 0:
            errors.append('Name is required.')
        if len(form_data['title'])== 0:
            errors.append('Title is required.')
        if len(form_data['category'])== 0:
            errors.append('Category is required.')
        
        return errors

#book is only going to have ONE author, but an author can have MANY books.
#so where to put the key? i'm going to say that since my book is going to   rely on the author the book is going to have the key.
    def createBook(self, form_data, author):
#create a method inside bookManager for creating a book...
        book = Book.objects.create(
            title = form_data['title'],
            category = form_data['category'],
            #author is the relationship of a foreign key
            author = author,
        )

        return book

class Book(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    #ONE - MANY rel key so it is going to be a ForeignKey
    #we want book to have a relationship with the Author class so...(Author, going to define the reverse index, or def the rel with the Author as well) and the related name is going to be the ref to all of the authors books.
    author = models.ForeignKey(Author, related_name="books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
#cancel server and run migrations
#& then run server again

    objects = BookManager()