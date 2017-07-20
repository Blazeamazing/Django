from django.shortcuts import render
# from .models import Users

# Create your views here.

def index(request):
    
    return render(request, 'brick_apps/index.html')