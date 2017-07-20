from django.shortcuts import render

# Create your views here.
def index(request):
    print(request.method)
    return render(request,'blaze_portfolio/index.html')

def about_me(request):
    print(request.method)
    return render(request,'blaze_portfolio/about_me.html')

def projects(request):
    print(request.method)
    return render(request,'blaze_portfolio/projects.html')

def testimonials(request):
    print(request.method)
    return render(request,'blaze_portfolio/testimonials.html')