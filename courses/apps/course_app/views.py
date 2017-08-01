from django.shortcuts import render, redirect
from .models import Course

# Create your views here.
def index(request):
    
    context = {
        "courses" : Course.objects.all()
    }

    return render(request, 'course_app/index.html', context)

def create(request):
    print (request.method)
    if request.method == "POST":
        
        errors = Course.objects.validate(request.POST)
        
        if not errors:
            Course.objects.create(name=request.POST['name'], comment=request.POST['comment'])

        print errors

    return redirect('/')
