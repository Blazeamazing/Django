from django.shortcuts import render, redirect
from .models import User, Post
#from .models import


# Create your views here.
def index(request):
    users = User.objects.all()

    context = {
        'users' : users,
    }

    return render(request, 'blogs_apps/index.html', context)