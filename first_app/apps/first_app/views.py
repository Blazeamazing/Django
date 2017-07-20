from django.shortcuts import render

# Create your views here.
# here is our first change with Django
# all of them will have this (request) method
def index(request):


                            # this is the path to our template
    return render(request, 'first_app/index.html')