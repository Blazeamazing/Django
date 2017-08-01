from django.shortcuts import render, redirect
from .models import Book, Author

# Create your views here.
def index(request):
    books = Book.objects.all()
    #need to grab all this book data from my view and pass it over into my html by using a dictionary called:  context
    context = {
        #key name books, and pass the dictionary as my third argument to render. then access 'books' key inside html.
        'books': books,
    }

    return render(request, 'book_app/index.html', context)

def create(request):
    #Class.objects - run query methods:get, filter, create. name from form
    if request.method == 'POST':
        
        errors = Book.objects.validate(request.POST)
#if there are no errors then i can print my data
        if not errors:
            #move these to models under author
            # name = request.POST['name']
            # author = Author.objects.create(name=name)
            author = Author.objects.createAuthor(request.POST)

    #this is being pulled over to models to keep views skinny. same goes for the above content
            # book = Book.objects.create(
            #     title = request.POST['title'],
            #     category = request.POST['category'],
            #     #author is the relationship of a foreign key
            #     author = author,
            # )
            book = Book.objects.createBook(request.POST, author)

        print errors

    return redirect('/')