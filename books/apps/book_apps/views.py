from django.shortcuts import render
from .models import Books

# Create your views here.
def index(request):
    Books.objects.create(title="20,000 Leagues Under the Sea", author="Jules Verne", published="December 23, 1954", category="Classic Fiction")
    books = Books.objects.all()
    print (books)
    return render(request,"book_apps/index.html")

# --->Example<---
# def index(request):
#     People.objects.creat(first_name="Blaze", last_name="Hayes")
#     people = People.objects.all()
#     print (people)
#     render(request, "third_app/index.html")