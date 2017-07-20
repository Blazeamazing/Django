from __future__ import unicode_literals
from django.db import models

# Create you models here:

class Books(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    published = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=30)


# Optional Assignment: Books and Authors
# Build on your previous assignment. Make a new table for authors with the assumption that each book can have only one author. How will your book table change? Be sure you can add a book and an author and the relationship between them.

# To Do:
# 1. Create your new database model and make any needed changes to your Book model.

# 2. Migrate!

# 3. Open shell.

# 4. Create 5 new books.

# 5. Create 5 new authors.

# 6. Assign author #1 to the first 2 books.

# 7. Assign author #4 to the rest of the books.